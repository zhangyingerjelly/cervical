import torch.nn as nn
def conv3x3(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


def conv1x1(in_planes, out_planes, stride=1):
    """1x1 convolution"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)
    

class Bottleneck(nn.Module):
    

    def __init__(self, cfg,stride=1,downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = conv1x1(cfg[0],cfg[1])
        self.bn1 = nn.BatchNorm2d(cfg[1])
        self.conv2 = conv3x3(cfg[1],cfg[2],stride)
        self.bn2 = nn.BatchNorm2d(cfg[2])
        self.conv3 = conv1x1(cfg[2], cfg[3])
        self.bn3 = nn.BatchNorm2d(cfg[3])
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample is not None:
            identity = self.downsample(x)
        
        out += identity
        out = self.relu(out)

        return out

class ResNet(nn.Module):

    def __init__(self, zero_init_residual=False,cfg=None):
        super(ResNet, self).__init__()
        layers=[3, 4, 6, 3]
        block=Bottleneck
        num_classes=3
        if cfg is None:
            cfg=[[64,64,64,256,256],[64,64,256]*2,[128,128,512,512],[128,128,512]*3,[256,256,1024,1024],[256,256,1024]*5,[512,512,2048,2048],[512,512,2048]*2]
            
            cfg = [item for sub_list in cfg for item in sub_list]
        print('cfg',cfg)
        start1=0   #把前一层最后的输出拿过来
        end1=start1+4+3*2 #11
        start2=end1
        end2=end1+4+3*3
        start3=end2
        end3=end2+4+3*5
        start4=end3
        end4=end3+4+3*2
        
        
        self.conv1 = nn.Conv2d(3, cfg[0], kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = nn.BatchNorm2d(cfg[0])
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 1, layers[0],cfg[start1:end1+1])
        self.layer2 = self._make_layer(block, 2, layers[1],cfg[start2:end2+1],stride=2)
        self.layer3 = self._make_layer(block, 3, layers[2],cfg[start3:end3+1],stride=2)
        self.layer4 = self._make_layer(block, 4, layers[3], cfg[start4:end4+1],stride=2)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(cfg[-1], num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        # Zero-initialize the last BN in each residual branch,
        # so that the residual branch starts with zeros, and each residual block behaves like an identity.
        # This improves the model by 0.2~0.3% according to https://arxiv.org/abs/1706.02677
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, Bottleneck):
                    nn.init.constant_(m.bn3.weight, 0)

    def _make_layer(self, block, id, blocks, cfg,stride=1):
        
        downsample = nn.Sequential(
            conv1x1(cfg[0], cfg[4], stride=stride),
            nn.BatchNorm2d(cfg[4]),
        )

        layers = []
        layers.append(block( cfg[0:4],stride, downsample))
        
        for i in range(1, blocks): #每个需要4个
            layers.append(block(cfg[4+(i-1)*3:8+(i-1)*3]))

        return nn.Sequential(*layers)

    def forward(self, x):
        
        x = self.conv1(x)
        
        x = self.bn1(x)
        x = self.relu(x)
        
        x = self.maxpool(x)
        

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x

