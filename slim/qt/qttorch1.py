<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>qttorch1.py (editing)</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon-file.ico?v=e2776a7f45692c839d6eea7d7ff6f3b2">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=3c2a865c832a1322285c55c6ed99abb2" type="text/css" />
    <link rel="stylesheet" href="/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=7afb461de36accb1aa133a1710f5bc56" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="/static/components/codemirror/lib/codemirror.css?v=fc217d502b05f65616356459c0ec1d62">
<link rel="stylesheet" href="/static/components/codemirror/addon/dialog/dialog.css?v=c89dce10b44d2882a024e7befc2b63f5">

    <link rel="stylesheet" href="/static/style/style.min.css?v=e91a43337d7c294cc9fab2938fa723b3" type="text/css"/>
    

    <link rel="stylesheet" href="/custom/custom.css" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/react/react.production.min.js?v=34f96ffc962a7deecc83037ccb582b58" type="text/javascript"></script>
    <script src="/static/components/react/react-dom.production.min.js?v=b14d91fb641317cda38dbc9dbf985ab4" type="text/javascript"></script>
    <script src="/static/components/create-react-class/index.js?v=94feb9971ce6d26211729abc43f96cd2" type="text/javascript"></script>
    <script src="/static/components/requirejs/require.js?v=951f856e81496aaeec2e71a1c2c0d51f" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200507104144",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"locale_data": {"nbjs": {"": {"domain": "nbjs"}, "Overwrite": ["\u91cd\u5199"], "undo": ["\u64a4\u9500"], "Scroll the current cell to the center": ["\u628a\u5f53\u524d\u5355\u5143\u683c\u6eda\u52a8\u5230\u4e2d\u95f4"], "show the header": ["\u663e\u793a\u6807\u9898"], "The checkpoint was last updated at:": ["\u8fd9\u4e2a\u4ee3\u7801\u6700\u540e\u66f4\u65b0\u65f6\u95f4:"], "select next cell": ["\u9009\u62e9\u4e0b\u4e00\u4e2a\u4ee3\u7801\u5757"], "Failed to retrieve MathJax from '%s'": ["\u4ece '%s' \u4e2d\u672a\u80fd\u68c0\u7d22 MathJax"], "The server is running on this version of Python:": ["\u8be5\u670d\u52a1\u8fd0\u884c\u4e2d\u4f7f\u7528\u7684python\u7248\u672c\u4e3a:"], "The notebook also failed validation:": ["\u4ee3\u7801\u5931\u8d25\u4e86:"], "The error was: %s": ["\u9519\u8bef; %s"], "Notebook converted": ["\u4ee3\u7801\u88ab\u4fee\u6539\u4e86"], "Rename the current notebook": ["\u91cd\u547d\u540d"], "To cancel a computation in progress, you can click here.": ["\u8981\u53d6\u6d88\u6b63\u5728\u8fdb\u884c\u7684\u8ba1\u7b97\uff0c\u60a8\u53ef\u4ee5\u70b9\u51fb\u8fd9\u91cc\u3002"], "restart the kernel, then re-run the whole notebook (with dialog)": ["\u91cd\u542f\u670d\u52a1, \u7136\u540e\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u4ee3\u7801(\u542b\u7a97\u53e3)"], "Keyboard Shortcuts": ["\u5feb\u6377\u952e"], "Notebook Menubar": ["\u83dc\u5355\u680f"], "The notebook file has changed on disk since the last time we opened or saved it. Do you want to overwrite the file on disk with the version open here, or load the version on disk (reload the page)?": ["\u81ea\u4ece\u4e0a\u6b21\u6211\u4eec\u6253\u5f00\u6216\u4fdd\u5b58\u5b83\u4ee5\u6765, \u7b14\u8bb0\u672c\u6587\u4ef6\u5df2\u7ecf\u5728\u78c1\u76d8\u4e0a\u53d1\u751f\u4e86\u53d8\u5316. \u60a8\u662f\u5426\u5e0c\u671b\u5728\u78c1\u76d8\u4e0a\u4f7f\u7528\u6253\u5f00\u7684\u7248\u672c, \u6216\u5728\u78c1\u76d8\u4e0a\u7684\u7248\u672c(\u91cd\u65b0\u52a0\u8f7d\u9875\u9762)\u4e0a\u8986\u76d6\u8be5\u6587\u4ef6?"], "go to cell start": ["\u8df3\u5230\u5355\u5143\u683c\u8d77\u59cb\u5904"], "An error occurred while creating a new notebook.": ["\u5f53\u521b\u5efa\u65b0\u7684notebook\u7684\u65f6\u5019\u51fa\u73b0\u4e00\u4e2a\u9519\u8bef."], "extend selection below": ["\u6269\u5c55\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "Restarting kernel": ["\u91cd\u542f\u670d\u52a1"], "Checkpoint delete failed": ["checkpoint\u5220\u9664\u5931\u8d25"], "Restart kernel?": ["\u91cd\u542f\u670d\u52a1?"], "indent": ["\u7f29\u8fdb"], "Revert notebook to checkpoint": ["\u6062\u590d\u4ee3\u7801"], "run all cells below": ["\u8fd0\u884c\u4e0b\u9762\u6240\u6709\u7684\u4ee3\u7801\u5757"], "go to cell end": ["\u8df3\u5230\u5355\u5143\u683c\u6700\u540e"], "PageUp": ["\u4e0a\u4e00\u9875"], "Edit Attachments": ["\u7f16\u8f91\u9644\u4ef6"], "You can use the left and right arrow keys to go backwards and forwards.": ["\u4f60\u53ef\u4ee5\u4f7f\u7528\u5de6\u53f3\u7bad\u5934\u952e\u6765\u524d\u540e\u79fb\u52a8"], "undo cell deletion": ["\u64a4\u9500\u5220\u9664"], "Use regex (JavaScript regex syntax)": [""], "Checkpoint restore failed": ["checkpoint \u91cd\u65b0\u4fdd\u5b58\u5931\u8d25"], "Toggle the hidden state of all output areas": ["\u5207\u6362\u6240\u6709\u8f93\u51fa\u533a\u57df\u7684\u9690\u85cf\u72b6\u6001"], "show the current docstring in pager (press shift-tab 4 times)": [""], "An invalid notebook may not function properly. The validation error was:": ["\u65e0\u6548\u7684\u7b14\u8bb0\u672c\u53ef\u80fd\u4e0d\u80fd\u6b63\u5e38\u5de5\u4f5c. \u9a8c\u8bc1\u9519\u8bef:"], "This notebook has been converted from a newer notebook format to the current notebook format v(%s).": ["\u8fd9\u4e2a\u7b14\u8bb0\u672c\u5df2\u7ecf\u4ece\u4e00\u79cd\u65b0\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u8f6c\u6362\u4e3a\u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f v(%s)."], "Home": ["Home"], "Invalid file name": ["\u65e0\u6548\u7684\u6587\u4ef6\u540d"], "Saving every %d sec.": ["\u6bcf\u9694 %s \u79d2\u4fdd\u5b58\u4e00\u6b21."], "Autosave Failed!": ["\u81ea\u52a8\u4fdd\u5b58\u5931\u8d25!"], "scroll notebook down": ["\u5411\u4e0b\u6eda\u52a8"], "Math/LaTeX rendering will be disabled.": ["Math/LaTeX \u6e32\u67d3 \u5c06\u4f1a\u5931\u6548."], "paste cell attachments": ["\u7c98\u8d34\u4ee3\u7801\u5757"], "close the pager": ["\u5173\u95ed\u9875\u9762"], "insert cell above": ["\u5728\u4e0a\u9762\u63d2\u5165\u4ee3\u7801\u5757"], "The next time you save this notebook, the current notebook format will be used.": ["\u4e0b\u6b21\u4f60\u4fdd\u5b58\u8fd9\u4e2a\u7b14\u8bb0\u672c\u65f6, \u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u5c06\u4f1a\u88ab\u4f7f\u7528."], "Edit Shortcuts": ["\u7f16\u8f91\u5feb\u6377\u952e"], "Notebook Toolbar": ["\u4ee3\u7801\u5de5\u5177\u680f"], "interrupt the kernel": ["\u4e2d\u65ad\u670d\u52a1"], "no checkpoint": ["\u6ca1\u6709\u68c0\u67e5\u70b9"], "The Kernel is busy, outputs may be lost.": ["\u670d\u52a1\u6b63\u5fd9, \u8f93\u51fa\u4e5f\u8bb8\u4f1a\u4e22\u5931."], "Rename file": ["\u6587\u4ef6\u91cd\u547d\u540d"], "Alt": ["Alt"], "Edit the tags": ["\u7f16\u8f91tags"], "delete word before": ["\u5220\u9664\u524d\u9762\u7684\u5355\u8bcd"], "Command Mode (press %s to enable)": ["\u547d\u4ee4\u884c\u6a21\u5f0f(\u6309 %s \u751f\u6548)"], "Trust the current notebook": ["\u4fe1\u4efb\u5f53\u524d\u4ee3\u7801"], "show all line numbers": ["\u663e\u793a\u884c\u53f7"], "Find": ["\u67e5\u627e"], "Kernel is not running": ["\u670d\u52a1\u6ca1\u6709\u8fd0\u884c"], "Enter": ["Enter"], "toggle header": ["\u5207\u6362\u6807\u9898"], "enter edit mode": ["\u8fdb\u5165\u7f16\u8f91\u6a21\u5f0f"], "enter command mode": ["\u8fdb\u5165\u547d\u4ee4\u884c\u6a21\u5f0f"], "extend selection above": ["\u6269\u5c55\u4e0a\u9762\u7684\u4ee3\u7801\u5757"], "merge selected cells, or current cell with cell below if only one cell is selected": ["\u5408\u5e76\u9009\u4e2d\u5355\u5143\u683c, \u5982\u679c\u53ea\u6709\u4e00\u4e2a\u5355\u5143\u683c\u88ab\u9009\u4e2d"], "toggle output scrolling of selected cells": ["\u5207\u6362\u9009\u5b9a\u5355\u5143\u7684\u8f93\u51fa\u6eda\u52a8"], "Warning: accessing Cell.cm_config directly is deprecated.": ["\u8b66\u544a: \u8bbf\u95eeCell.cm_config\u5df2\u7ecf\u88ab\u5f03\u7528\u4e86."], "emacs-style line kill": [""], "Rename": ["\u91cd\u547d\u540d"], "Revert": ["\u6062\u590d"], "Restoring to checkpoint...": ["\u91cd\u65b0\u4fdd\u5b58checkpoint..."], "The notebook list is empty.": ["\u4ee3\u7801\u5217\u8868\u4e3a\u7a7a, \u8bf7\u6dfb\u52a0\u4ee3\u7801."], "Don't Restart": ["\u4e0d\u8981\u91cd\u542f"], "Creating Folder Failed": ["\u521b\u5efa\u6587\u4ef6\u5939\u5931\u8d25"], "Last Checkpoint: %s": ["\u6700\u540e\u68c0\u67e5: %s "], "run all cells above": ["\u8fd0\u884c\u4e0a\u9762\u6240\u6709\u7684\u4ee3\u7801\u5757"], "This cannot be undone.": ["\u8be5\u64cd\u4f5c\u4e0d\u80fd\u88ab\u6267\u884c."], "Replace All": ["\u66ff\u6362\u6240\u6709"], "Return": ["\u8fd4\u56de"], "Shutdown kernel?": ["\u5173\u95ed\u670d\u52a1"], "Notebook copy failed": ["\u4ee3\u7801\u590d\u5236\u5931\u8d25"], "The error was: ": ["\u9519\u8bef: "], "run cell and select next": ["\u8fd0\u884c\u4ee3\u7801\u5757\u5e76\u4e14\u9009\u62e9\u4e0b\u4e00\u4e2a\u4ee3\u7801\u5757"], "here": ["\u8fd9\u91cc"], "Notebook loaded": ["\u7a0b\u5e8f\u5df2\u52a0\u8f7d"], "split cell at cursor": ["\u5728\u9f20\u6807\u5904\u5206\u5272\u4ee3\u7801\u5757"], "Clear the content of all the outputs": ["\u6e05\u7a7a\u6240\u6709\u7684\u8f93\u51fa\u5185\u5bb9"], "A trusted Jupyter notebook may execute hidden malicious code when you open it. Selecting trust will immediately reload this notebook in a trusted state. For more information, see the Jupyter security documentation: ": ["\u5f53\u4f60\u6253\u5f00\u5b83\u65f6, \u4e00\u4e2a\u53ef\u4fe1\u4efb\u7684Jupyter\u7b14\u8bb0\u672c\u53ef\u80fd\u4f1a\u6267\u884c\u9690\u85cf\u7684\u6076\u610f\u4ee3\u7801. \u9009\u62e9\u4fe1\u4efb\u5c06\u7acb\u5373\u5728\u4e00\u4e2a\u53ef\u4fe1\u7684\u72b6\u6001\u4e2d\u91cd\u65b0\u52a0\u8f7d\u8fd9\u4e2a\u7b14\u8bb0\u672c. \u8981\u4e86\u89e3\u66f4\u591a\u4fe1\u606f, \u8bf7\u53c2\u9605Jupyter\u5b89\u5168\u6587\u6863:"], "Failed to read file": ["\u8bfb\u53d6\u6587\u4ef6\u5931\u8d25"], "Back to Command Mode": ["\u8f6c\u5230\u547d\u4ee4\u6a21\u5f0f"], "save notebook": ["\u4fdd\u5b58\u4ee3\u7801"], "Kernel not found": ["\u670d\u52a1\u6ca1\u627e\u5230"], "Notice that the border around the currently active cell changed color. Typing will insert text into the currently active cell.": ["\u8bf7\u6ce8\u610f, \u5f53\u524d\u6d3b\u52a8\u5355\u5143\u5468\u56f4\u7684\u8fb9\u6846\u6539\u53d8\u4e86\u989c\u8272. \u952e\u5165\u5c06\u5728\u5f53\u524d\u6d3b\u52a8\u5355\u5143\u4e2d\u63d2\u5165\u6587\u672c."], "run selected cells": ["\u8fd0\u884c\u9009\u4e2d\u7684\u4ee3\u7801\u5757"], "merge cell above": ["\u5408\u5e76\u4e0a\u9762\u7684\u5355\u5143\u683c"], "Interrupting the Kernel": ["\u5185\u6838\u4e2d\u65ad"], "trust notebook": ["\u4fe1\u4efb\u4ee3\u7801"], "Connecting to kernel": ["\u6b63\u5728\u8fde\u63a5\u670d\u52a1"], "Open the pager in an external window": ["\u5728\u5185\u90e8\u7a97\u53e3\u6253\u5f00\u9875\u9762"], "Open in Pager": [""], "(unsaved changes)": ["(\u672a\u4fdd\u5b58\u6539\u53d8)"], "Kernel Indicator": ["\u5185\u6838\u6307\u793a\u5668"], "restart the kernel (with dialog)": ["\u91cd\u542f\u670d\u52a1(\u5e26\u7a97\u53e3)"], "duplicate notebook": ["\u590d\u5236\u4ee3\u7801"], "hide all line numbers": ["\u9690\u85cf\u884c\u53f7"], "About Jupyter Notebook": ["\u5173\u4e8e Jupyter Notebook"], "More than 100 matches, aborting": ["\u8d85\u8fc7100\u4e2a\u5339\u914d, \u4e2d\u6b62"], "scroll cell center": ["\u6eda\u52a8\u5230\u5355\u5143\u683c\u4e2d\u95f4"], "In": [""], " We recommend putting custom metadata attributes in an appropriately named substructure, so they don't conflict with those of others.": ["\u6211\u4eec\u5efa\u8bae\u5c06\u81ea\u5b9a\u4e49\u7684\u5143\u6570\u636e\u5c5e\u6027\u653e\u5165\u9002\u5f53\u7684\u5b50\u7ed3\u6784\u4e2d\uff0c\u8fd9\u6837\u5c31\u4e0d\u4f1a\u4e0e\u5176\u4ed6\u7684\u5b50\u7ed3\u6784\u53d1\u751f\u51b2\u7a81."], "## This is a level 2 heading": ["## \u8fd9\u662f\u4e00\u4e2a 2 heading"], "Newer Notebook": ["\u65b0\u7b14\u8bb0"], "Notebook failed to load": ["\u4ee3\u7801\u52a0\u8f7d\u5931\u8d25"], "change cell to heading 2": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 2"], "run all cells": ["\u8fd0\u884c\u6240\u6709\u7684\u4ee3\u7801\u5757"], "Unrecognized output: %s": ["\u672a\u8bc6\u522b\u7684\u8f93\u51fa: %s"], "Waiting for kernel to be available...": ["\u7b49\u5f85\u670d\u52a1\u53ef\u7528..."], "Error in cell toolbar callback %s": ["\u5de5\u5177\u680f\u8c03\u7528 %s \u51fa\u73b0\u9519\u8bef"], "Open a dialog to edit the command mode keyboard shortcuts": ["\u6253\u5f00\u7a97\u53e3\u6765\u7f16\u8f91\u5feb\u6377\u952e"], "Attachments": ["\u9644\u4ef6"], "Current Kernel Information:": ["\u5f53\u524d\u670d\u52a1\u4fe1\u606f:"], "unrecognized cell type:": ["\u672a\u8bc6\u522b\u7684\u5355\u5143\u683c\u7c7b\u578b:"], "Notebook saved": ["\u4ee3\u7801\u5df2\u4fdd\u5b58"], "The kernel has died, and the automatic restart has failed. It is possible the kernel cannot be restarted. If you are not able to restart the kernel, you will still be able to save the notebook, but running code will no longer work until the notebook is reopened.": ["\u5185\u6838\u5df2\u7ecf\u6b7b\u4ea1\uff0c\u81ea\u52a8\u91cd\u542f\u4e5f\u5931\u8d25\u4e86\u3002\u6709\u53ef\u80fd\u5185\u6838\u4e0d\u80fd\u91cd\u65b0\u542f\u52a8\u3002\u5982\u679c\u60a8\u4e0d\u80fd\u91cd\u65b0\u542f\u52a8\u5185\u6838\uff0c\u60a8\u4ecd\u7136\u80fd\u591f\u4fdd\u5b58\u7b14\u8bb0\u672c\uff0c\u4f46\u662f\u8fd0\u884c\u4ee3\u7801\u5c06\u4e0d\u518d\u5de5\u4f5c\uff0c\u76f4\u5230\u7b14\u8bb0\u672c\u91cd\u65b0\u6253\u5f00. "], "The menubar has menus for actions on the notebook, its cells, and the kernel it communicates with.": ["\u83dc\u5355\u680f\u64cd\u4f5c\u754c\u9762, \u5b83\u7684\u5355\u5143\u683c\u548c\u5b83\u4e0e\u4e4b\u901a\u4fe1\u7684\u5185\u6838\u4e0a\u8fdb\u884c\u64cd\u4f5c. "], "restart kernel and clear output": ["\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u6e05\u7a7a\u8f93\u5165"], "Failed to read file %s": ["\u8bfb\u53d6\u4ee3\u7801\u6587\u4ef6 %s \u5931\u8d25\u4e86."], "Cancel": ["\u53d6\u6d88"], "Page Up": ["\u4e0a\u4e00\u9875"], "Click here to rename, delete, etc.": ["\u70b9\u51fb\u8fdb\u884c\u64cd\u4f5c."], "Reload": ["\u91cd\u8f7d"], "Edit Metadata": ["\u7f16\u8f91\u5143\u6570\u636e"], "Current cell attachments": ["\u5f53\u524d\u5757\u9644\u4ef6"], "No kernel": ["\u6ca1\u6709\u670d\u52a1"], "Edit Mode": ["\u7f16\u8f91\u6a21\u5f0f"], "Ctrl": ["Ctrl"], "delete line right of cursor": [""], "Shift": ["Shift"], "Control": ["\u63a7\u5236"], "toggle rtl layout": ["\u5207\u6362trl\u5e03\u5c40"], "toggle output of selected cells": ["\u9009\u62e9\u5355\u5143\u683c\u7684\u8f93\u51fa"], "Jupyter Pager": ["Jupyter \u9875\u9762"], "Edit attachments": ["\u7f16\u8f91\u9644\u4ef6"], "hide the toolbar": ["\u9690\u85cf\u5de5\u5177\u680f"], "Older versions of Jupyter may not be able to read the new format.": ["\u65e7\u7248\u672c\u7684Jupyter\u53ef\u80fd\u65e0\u6cd5\u8bfb\u53d6\u65b0\u683c\u5f0f."], "Kernel starting, please wait...": ["\u670d\u52a1\u6b63\u5728\u542f\u52a8,\u8bf7\u7b49\u5f85..."], "The Jupyter Notebook has two different keyboard input modes.": ["Jupyter\u7b14\u8bb0\u672c\u6709\u4e24\u79cd\u4e0d\u540c\u7684\u952e\u76d8\u8f93\u5165\u6a21\u5f0f."], "Tooltip will linger for 10 seconds while you type": [""], "An error occurred while renaming \"%1$s\" to \"%2$s\".": ["\u5f53\u628a \"%1$s\" \u91cd\u547d\u540d\u4e3a \"%2$s\" \u65f6\u51fa\u73b0\u9519\u8bef."], "(No name)": ["(\u6ca1\u6709\u540d\u5b57)"], "Pressing <code>Esc</code> or clicking outside of the input text area takes you back to Command Mode.": ["\u6309\u4e0b<code>Esc</code>, \u6216\u8005\u70b9\u51fb\u8f93\u5165\u6587\u672c\u533a\u57df, \u5c06\u4f60\u8fd4\u56de\u5230\u547d\u4ee4\u6a21\u5f0f. "], "move cells down": ["\u4e0b\u79fb"], "Enter a new file name:": ["\u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u6587\u4ef6\u540d:"], "Close": ["\u5173\u95ed"], "show the toolbar": ["\u663e\u793a\u5de5\u5177\u680f"], "Create and open a copy of the current notebook": ["\u521b\u5efa\u5e76\u6253\u5f00\u5f53\u524d\u4ee3\u7801\u7684\u4e00\u4e2a\u526f\u672c"], "select all": ["\u5168\u9009"], "Are you sure you want to duplicate: \"%s\"?": ["\u786e\u5b9a\u590d\u5236: \"%s\"?", "\u786e\u5b9a\u590d\u5236: \u5df2\u9009\u62e9 %d \u6587\u4ef6?"], "Edit Notebook Attachments": ["\u7f16\u8f91\u4ee3\u7801\u9644\u4ef6"], "Set Kernel": ["\u8bbe\u7f6e\u670d\u52a1"], "Rename Notebook": ["\u91cd\u547d\u540d"], "Replace in selected cells": ["\u5728\u9009\u4e2d\u5355\u5143\u683c\u4e2d\u66ff\u6362"], "Match case": ["\u5339\u914d"], "merge cell below": ["\u5408\u5e76\u4e0b\u9762\u7684\u5355\u5143\u683c"], "Find and Replace": ["\u67e5\u627e\u5e76\u4e14\u66ff\u6362"], "Why is this needed? ": ["\u8fd9\u4e2a\u4e3a\u5565\u9700\u8981?"], "Creating File Failed": ["\u521b\u5efa\u6587\u4ef6\u5931\u8d25"], "Delete": ["\u5220\u9664"], "Unsaved changes will be lost.": ["\u672a\u4fdd\u5b58\u7684\u4fee\u6539\u5c06\u4f1a\u4e22\u5931."], "move selected cells down": ["\u4e0b\u79fb\u9009\u4e2d\u5355\u5143\u683c"], "You can still work with this notebook, but cell and output types introduced in later notebook versions will not be available.": ["\u60a8\u4ecd\u7136\u53ef\u4ee5\u4f7f\u7528\u672c\u7a0b\u5e8f, \u4f46\u662f\u5728\u4ee5\u540e\u7684\u7248\u672c\u4e2d\u5f15\u5165\u7684\u5355\u5143\u548c\u8f93\u51fa\u7c7b\u578b\u5c06\u4e0d\u53ef\u7528."], "Edit the metadata": ["\u7f16\u8f91\u5143\u6570\u636e"], "Command": ["\u547d\u4ee4"], "Restore": ["\u91cd\u65b0\u4fdd\u5b58"], "Can't execute cell since kernel is not set.": ["\u53ea\u8981\u670d\u52a1\u6ca1\u6709\u8bbe\u7f6e\u5c31\u4e0d\u80fd\u6267\u884c\u5355\u5143\u683c\u4ee3\u7801."], "Scroll the current cell to the top": ["\u5c06\u5f53\u524d\u5355\u5143\u683c\u6eda\u52a8\u5230\u9876\u90e8"], "insert image": ["\u63d2\u5165\u56fe\u7247"], "Option": ["\u9009\u9879"], "Kernel ready": ["\u670d\u52a1\u51c6\u5907\u597d\u4e86"], "Restart kernel and clear all output?": ["\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u6e05\u7a7a\u8f93\u51fa?"], "The save operation succeeded, but the notebook does not appear to be valid. The validation error was:": ["\u4fdd\u5b58\u64cd\u4f5c\u6210\u529f\u4e86, \u4f46\u662f\u8fd9\u4e2a\u7b14\u8bb0\u672c\u770b\u8d77\u6765\u5e76\u4e0d\u6709\u6548. \u9a8c\u8bc1\u9519\u8bef:"], "confirm restart kernel": ["\u786e\u5b9a\u91cd\u542f\u670d\u52a1"], "toggle cell scrolling": ["\u5207\u6362\u5355\u5143\u6eda\u52a8"], "Command Mode": ["\u547d\u4ee4 \u6a21\u5f0f"], "No checkpoints": ["\u6ca1\u6709\u68c0\u67e5\u70b9"], "delete word after": ["\u5220\u9664\u540e\u9762\u7684\u5355\u8bcd"], "Edit Cell Attachments": ["\u7f16\u8f91\u5757\u9644\u4ef6"], "clear all cells output": ["\u6e05\u7a7a\u6240\u6709\u5355\u5143\u683c\u8f93\u51fa"], "An error occurred while deleting \"%s\".": ["\u5f53\u5220\u9664 \"%s\" \u65f6, \u51fa\u73b0\u9519\u8bef."], "hide line numbers in all cells, and persist the setting": ["\u9690\u85cf\u884c\u53f7\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "%d match": ["%d \u5339\u914d", "%d \u5339\u914d"], "scroll notebook up": ["\u5411\u4e0a\u6eda\u52a8"], "change cell to heading 4": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 4"], "restart kernel": ["\u91cd\u542f\u670d\u52a1"], "rename notebook": ["\u91cd\u547d\u540d"], "Do you want to shutdown the current kernel?  All variables will be lost.": ["\u5982\u679c\u5173\u95ed\u670d\u52a1\uff0c\u6240\u6709\u53d8\u91cf\u90fd\u4f1a\u4e22\u5931"], "tooltip": ["\u5de5\u5177\u63d0\u793a"], "merge cell with next cell": ["\u5408\u5e76\u4e0b\u4e00\u4e2a\u5355\u5143\u683c"], "Kernel Dead": ["\u670d\u52a1\u6302\u6389"], "restart the kernel and clear all output (no confirmation dialog)": ["\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u6e05\u7a7a\u6240\u6709\u8f93\u51fa(\u4e0d\u542b\u786e\u8ba4\u7a97\u53e3)"], "None": [""], "The file size is %d MB. Do you still want to upload it?": ["\u6587\u4ef6\u5927\u5c0f\u4e3a %d MB, \u8fd8\u60f3\u4e0a\u4f20\u4e48?"], "Select a file": ["\u9009\u62e9\u6587\u4ef6"], "Some features of the original notebook may not be available.": ["\u539f\u59cb\u7b14\u8bb0\u672c\u7684\u4e00\u4e9b\u7279\u6027\u53ef\u80fd\u65e0\u6cd5\u4f7f\u7528."], "<b>Edit mode</b> allows you to type code or text into a cell and is indicated by a green cell border.": ["<b>\u7f16\u8f91\u6a21\u5f0f</b>\u5141\u8bb8\u60a8\u5c06\u4ee3\u7801\u6216\u6587\u672c\u8f93\u5165\u5230\u4e00\u4e2a\u5355\u5143\u683c\u4e2d\uff0c\u5e76\u901a\u8fc7\u4e00\u4e2a\u7eff\u8272\u7684\u5355\u5143\u683c\u6765\u8868\u793a"], "Restart kernel and re-run the whole notebook?": ["\u91cd\u65b0\u542f\u52a8\u5185\u6838\u5e76\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u7b14\u8bb0\u672c?"], "restart the kernel, then re-run the whole notebook (no confirmation dialog)": ["\u91cd\u542f\u670d\u52a1, \u7136\u540e\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u4ee3\u7801(\u4e0d\u542b\u786e\u8ba4\u7a97\u53e3)"], "Not Trusted": ["\u4e0d\u53ef\u4fe1"], "Are you sure you want to permanently delete: \"%s\"?": ["\u5220\u9664\u4e0d\u53ef\u6062\u590d: \"%s\", \u786e\u5b9a\u5220\u9664?", "\u5220\u9664\u4e0d\u53ef\u6062\u590d: \u9009\u62e9 %d \u6587\u4ef6, \u786e\u5b9a\u5220\u9664?"], "Checkpoint created": ["checkpoint\u5df2\u521b\u5efa"], "Rename directory": ["\u91cd\u547d\u540d\u8def\u5f84"], "copy selected cells": ["\u590d\u5236\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "Custom": [""], "Failed to start the kernel": ["\u542f\u52a8\u670d\u52a1\u5931\u8d25"], "Notebook changed": ["\u7b14\u8bb0\u6539\u53d8\u4e86"], "delete whole line": ["\u5220\u9664\u6574\u884c"], "select cell above": ["\u9009\u62e9\u4e0a\u9762\u7684\u4ee3\u7801\u5757"], "Minus": [""], "edit command mode keyboard shortcuts": ["\u7f16\u8f91\u547d\u4ee4\u6a21\u5f0f\u5feb\u6377\u952e"], "show line numbers in all cells, and persist the setting": ["\u5728\u6240\u6709\u5355\u5143\u683c\u4e2d\u663e\u793a\u884c\u53f7\uff0c\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "Caps Lock": ["Caps Lock"], "No Connection to Kernel": ["\u6ca1\u6709\u5230\u670d\u52a1\u7684\u8fde\u63a5"], "Restart and Clear All Outputs": ["\u91cd\u542f\u5e76\u6e05\u7a7a\u6240\u6709\u8f93\u51fa"], "Move": ["\u79fb\u52a8"], "Javascript error adding output!": ["Javascript\u6dfb\u52a0\u8f93\u51fa\u9519\u8bef!"], "Only candidate for language: %1$s was %2$s.": ["\u53ea\u652f\u6301\u8bed\u8a00: %1$s - %2$s."], "Edit Tags": ["\u7f16\u8f91tags"], "Move Failed": ["\u79fb\u52a8\u5931\u8d25"], "Do you want to restart the current kernel?  All variables will be lost.": ["\u5982\u679c\u91cd\u542f\u670d\u52a1, \u6240\u6709\u53d8\u91cf\u90fd\u4f1a\u4e22\u5f03."], "restart the kernel (no confirmation dialog)": ["\u91cd\u542f\u670d\u52a1(\u6ca1\u6709\u786e\u8ba4\u7a97\u53e3)"], "An error occurred while moving \"%1$s\" from \"%2$s\" to \"%3$s\".": ["\u5f53\u628a \"%1$s\" \u4ece \"%2$s\" \u79fb\u52a8\u5230 \"%3$s\" \u65f6\u51fa\u73b0\u9519\u8bef."], "This concludes the Jupyter Notebook User Interface Tour.": ["\u8fd9\u5c31\u7ed3\u675f\u4e86Jupyter\u7b14\u8bb0\u672c\u7528\u6237\u754c\u9762\u4e4b\u65c5\u3002"], "Error loading notebook": ["\u52a0\u8f7d\u4ee3\u7801\u51fa\u9519"], "Trusted Notebook": ["\u53ef\u4fe1\u7684\u7b14\u8bb0"], "click to expand output": ["\u70b9\u51fb\u5c55\u5f00\u5185\u5bb9"], "Slideshow": ["\u5e7b\u706f\u7247"], "No matches, invalid or empty regular expression": ["\u6ca1\u5339\u914d\u5230, \u65e0\u6548\u6216\u7a7a\u7684\u6b63\u5219\u8868\u8fbe\u5f0f"], "cut selected cells": ["\u526a\u5207\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "Server Information:": ["\u670d\u52a1\u4fe1\u606f:"], "confirm restart kernel and run all cells": ["\u786e\u8ba4\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "Duplicate Failed": ["\u590d\u5236\u5931\u8d25"], "The kernel appears to have died. It will restart automatically.": ["\u670d\u52a1\u4f3c\u4e4e\u6302\u6389\u4e86,\u4f46\u662f\u4f1a\u7acb\u523b\u91cd\u542f\u7684."], "Opens in a new window": ["\u5728\u65b0\u7a97\u53e3\u6253\u5f00"], "Heading": ["\u6807\u9898"], "Upload": ["\u4e0a\u4f20"], "Select a file to insert.": ["\u9009\u62e9\u6587\u4ef6\u63d2\u5165"], "Use markdown headings": ["\u4f7f\u7528\u6807\u7b7e headings"], "extend selected cells below": ["\u6269\u5c55\u4e0b\u9762\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "The toolbar has buttons for the most common actions. Hover your mouse over each button for more information.": ["\u5de5\u5177\u680f\u6709\u6700\u5e38\u89c1\u64cd\u4f5c\u7684\u6309\u94ae\u3002\u5c06\u9f20\u6807\u60ac\u505c\u5728\u6bcf\u4e2a\u6309\u94ae\u4e0a\u4ee5\u83b7\u5f97\u66f4\u591a\u4fe1\u606f\u3002"], "There are no attachments for this cell.": ["\u8fd9\u4e2a\u5757\u6ca1\u6709\u9644\u4ef6."], "dedent": ["\u53d6\u6d88\u7f29\u8fdb"], "restart kernel and run all cells": ["\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "Right now you are in Command Mode, and many keyboard shortcuts are available. In this mode, no icon is displayed in the indicator area.": ["\u73b0\u5728\u4f60\u5904\u4e8e\u547d\u4ee4\u6a21\u5f0f, \u8bb8\u591a\u5feb\u6377\u952e\u90fd\u53ef\u4ee5\u4f7f\u7528. \u5728\u8be5\u6a21\u5f0f\u4e0b, \u6307\u793a\u533a\u57df\u4e2d\u6ca1\u6709\u663e\u793a\u56fe\u6807."], "Duplicate": ["\u590d\u5236"], "toggle line numbers": ["\u5207\u6362\u884c\u53f7"], "Welcome to the Notebook Tour": ["\u6b22\u8fce\u4f7f\u7528Notebook"], "Kernel Restarting": ["\u670d\u52a1\u6b63\u91cd\u542f"], "Loading notebook": ["\u52a0\u8f7d\u670d\u52a1"], "See the error console for details.": ["\u6709\u5173\u8be6\u7ec6\u4fe1\u606f, \u8bf7\u53c2\u9605\u9519\u8bef\u63a7\u5236\u53f0."], "Shutdown": ["\u5173\u95ed"], "This notebook has been converted from an older notebook format to the current notebook format v(%s).": ["\u672c\u7b14\u8bb0\u672c\u5df2\u4ece\u8f83\u65e7\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u8f6c\u6362\u4e3a\u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f v(%s)."], "Creating Notebook Failed": ["\u521b\u5efa\u4ee3\u7801\u5931\u8d25"], "paste cells above": ["\u7c98\u8d34\u5230\u4e0a\u9762"], "Are you sure you want to restart the current kernel and re-execute the whole notebook?  All variables and outputs will be lost.": ["\u60a8\u786e\u5b9a\u8981\u91cd\u65b0\u542f\u52a8\u5f53\u524d\u7684\u5185\u6838\u5e76\u91cd\u65b0\u6267\u884c\u6574\u4e2a\u7b14\u8bb0\u672c\u5417? \u6240\u6709\u7684\u53d8\u91cf\u548c\u8f93\u51fa\u90fd\u5c06\u4e22\u5931."], "Sub-Slide": ["\u5b50\u5e7b\u706f\u7247"], "edit command-mode keyboard shortcuts": ["\u7f16\u8f91\u547d\u4ee4\u884c\u5feb\u6377\u952e"], "Code": ["\u4ee3\u7801"], "Skip": ["\u8df3\u8fc7"], "This notebook is version %1$s, but we only fully support up to %2$s.": ["\u672c\u7a0b\u5e8f\u7248\u672c %1$s, \u4f46\u662f\u6211\u4eec\u53ea\u662f\u652f\u6301\u5230 %2$s."], "No Kernel": ["\u6ca1\u6709\u670d\u52a1"], "Toggle the scrolling state of all output areas": ["\u5207\u6362\u6240\u6709\u8f93\u51fa\u533a\u57df\u7684\u6eda\u52a8\u72b6\u6001"], "Right": ["\u53f3"], "We can't get paste events in this browser without a text box. ": ["\u5728\u6d4f\u89c8\u5668\u91cc\u6ca1\u6709\u6587\u672c\u6846\u6211\u4eec\u4e0d\u80fd\u7c98\u8d34. "], "Apply": ["\u5e94\u7528"], "File names must be at least one character and not start with a period": ["\u6587\u4ef6\u540d\u4e0d\u80fd\u4e3a\u7a7a...\u5e76\u4e14\u4e0d\u80fd\u4ee5\u53e5\u53f7\u5f00\u59cb,\u9664\u4e0b\u5212\u7ebf\u4ee5\u5916\u7684\u7b26\u53f7\u90fd\u4e0d\u80fd\u5f00\u5934..."], "Slide": ["\u5e7b\u706f\u7247"], "(autosaved)": ["(\u81ea\u52a8\u4fdd\u5b58)"], "change cell to code": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u4ee3\u7801"], "There's an invisible text box focused in this dialog.": ["\u5728\u8fd9\u4e2a\u5bf9\u8bdd\u6846\u4e2d\u6709\u4e00\u4e2a\u4e0d\u53ef\u89c1\u7684\u6587\u672c\u6846."], "select cell below": ["\u9009\u62e9\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "End of Tour": ["\u7ed3\u675f"], "Tab": ["Tab"], "Replace file": ["\u66ff\u6362\u6587\u4ef6"], "insert cell below": ["\u5728\u4e0b\u9762\u63d2\u5165\u4ee3\u7801\u5757"], "Keyboard shortcuts": ["\u5feb\u6377\u952e"], "copy cell attachments": ["\u590d\u5236\u4ee3\u7801\u5757"], "delete selected cells": ["\u5220\u9664\u9009\u4e2d\u5355\u5143\u683c"], "Interrupting kernel": ["\u6b63\u5728\u4e2d\u65ad\u670d\u52a1"], "Large file size warning": ["\u8bf7\u6ce8\u610f\u6587\u4ef6\u5927\u5c0f..."], "Do you want to restart the current kernel and clear all output?  All variables and outputs will be lost.": ["\u60a8\u662f\u5426\u5e0c\u671b\u91cd\u65b0\u542f\u52a8\u5f53\u524d\u7684\u5185\u6838\u5e76\u6e05\u9664\u6240\u6709\u8f93\u51fa? \u6240\u6709\u7684\u53d8\u91cf\u548c\u8f93\u51fa\u90fd\u5c06\u4e22\u5931."], "There is already a file named \"%s\". Do you want to replace it?": ["\u6587\u4ef6\u540d\u5df2\u7ecf\u5b58\u5728 \"%s\", \u9700\u8981\u66ff\u6362\u73b0\u6709\u6587\u4ef6?"], "run cell and insert below": ["\u8fd0\u884c\u4ee3\u7801\u5757\u5e76\u4e14\u63d2\u5165\u4e0b\u9762"], "Using kernel: ": ["\u4f7f\u7528\u670d\u52a1:"], "Slide Type": ["\u7c7b\u578b"], "Trusted": ["\u53ef\u4fe1\u7684"], "Enter a new notebook name:": ["\u8bf7\u8f93\u5165\u4ee3\u7801\u540d\u79f0:"], "Unknown error": ["\u672a\u77e5\u9519\u8bef"], "Enter a new directory name:": ["\u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u8def\u5f84:"], "%s to paste": ["%s \u6765\u7c98\u8d34"], "toggle overwrite flag": ["\u5207\u6362 \u91cd\u5199\u6807\u5fd7"], "Enter a new destination directory path for this item:": ["\u4e3a\u4ee3\u7801\u9009\u62e9\u4e00\u4e2a\u65b0\u7684\u8def\u5f84:", "\u4e3a\u9009\u4e2d\u7684 %d \u4ee3\u7801\u9009\u62e9\u4e00\u4e2a\u65b0\u7684\u8def\u5f84:"], "merge cells": ["\u5408\u5e76\u5355\u5143\u683c"], "Renaming...": ["\u6b63\u5728\u91cd\u547d\u540d..."], "undo selection": ["\u64a4\u9500\u9009\u62e9"], "merge selected cells": ["\u5408\u5e76\u9009\u4e2d\u7684\u5355\u5143\u683c"], "Kernel Created": ["\u670d\u52a1\u521b\u5efa"], "click to unscroll output; double click to hide": ["\u5355\u51fb\u663e\u793a\u8f93\u51fa; \u53cc\u51fb\u9690\u85cf"], "Trust": ["\u4fe1\u4efb"], "Grow the tooltip vertically (press shift-tab twice)": [""], "Continue Running": ["\u7ee7\u7eed\u8fd0\u884c"], "Autosave in progress, latest changes may be lost.": ["\u81ea\u52a8\u4fdd\u5b58, \u6700\u65b0\u7684\u6539\u53d8\u6709\u53ef\u80fd\u88ab\u4e22\u5f03."], "Dialog for paste from system clipboard": ["\u4ece\u7cfb\u7edf\u526a\u5207\u677f\u7c98\u8d34"], "Kernel Busy": ["\u670d\u52a1\u6b63\u5fd9"], "Toggle the screen directionality between left-to-right and right-to-left": ["\u5207\u6362\u5de6\u53f3\u81f3\u53f3\u81f3\u5de6\u4e4b\u95f4\u7684\u5c4f\u5e55\u65b9\u5411"], "Manually edit the JSON below to manipulate the metadata for this notebook.": ["\u624b\u52a8\u7f16\u8f91\u4e0b\u9762\u7684JSON\u4ee3\u7801\u6765\u4fee\u6539\u754c\u9762\u5143\u6570\u636e."], "The version of the notebook server is: ": ["\u8be5notebook \u670d\u52a1\u7684\u7248\u672c\u662f\uff1a"], "Messages in response to user actions (Save, Interrupt, etc.) appear here.": ["\u54cd\u5e94\u7528\u6237\u64cd\u4f5c(\u4fdd\u5b58, \u4e2d\u65ad\u7b49)\u7684\u6d88\u606f\u51fa\u73b0\u5728\u8fd9\u91cc."], "extend selected cells above": ["\u6269\u5c55\u4e0a\u9762\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "Trust Notebook": ["\u4fe1\u4efb\u7b14\u8bb0"], "clear cell output": ["\u6e05\u7a7a\u6240\u6709\u5355\u5143\u683c\u8f93\u51fa"], "Add tag": ["\u6dfb\u52a0\u6807\u7b7e"], "Markdown": ["\u6807\u8bb0"], "Up": ["\u4e0a"], "The Kernel indicator looks like this when the Kernel is busy.": ["\u5185\u6838\u6307\u793a\u5668\u5728\u5185\u6838\u7e41\u5fd9\u65f6\u770b\u8d77\u6765\u662f\u8fd9\u6837\u7684\u3002"], "Cell": ["\u5355\u5143\u683c"], "move selected cells up": ["\u4e0a\u79fb\u9009\u4e2d\u5355\u5143\u683c"], "comment": ["\u8bc4\u8bba"], "change cell to markdown": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u7b7e"], "You can click here to get a list of all of the keyboard shortcuts.": ["\u70b9\u51fb\u83b7\u5f97\u6240\u6709\u5feb\u6377\u952e"], "move cells up": ["\u4e0a\u79fb"], "toggle toolbar": ["\u5207\u6362\u5de5\u5177\u680f"], "Page Down": ["\u4e0b\u4e00\u9875"], "Connection failed": ["\u8fde\u63a5\u5931\u8d25"], "redo": ["\u91cd\u505a"], "Checkpoint failed": ["Checkpoint \u5931\u8d25"], "open the command palette": ["\u6253\u5f00\u547d\u4ee4\u914d\u7f6e"], "toggle all line numbers": ["\u5207\u6362\u6240\u6709\u884c\u53f7"], "Mode Indicator": ["\u6a21\u5f0f\u6307\u793a\u5668"], "restart the kernel and clear all output (with dialog)": ["\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u6e05\u7a7a\u6240\u6709\u8f93\u51fa(\u542b\u7a97\u53e3)"], "delete cells": ["\u5220\u9664\u5355\u5143\u683c"], "Create a new notebook with %s": ["\u521b\u5efa\u65b0\u7684\u4ee3\u7801 %s"], "go one word left": ["\u8df3\u5230\u5355\u8bcd\u5de6\u8fb9"], "ignore": ["\u5ffd\u7565"], "toggle cell output": ["\u5207\u6362\u5355\u5143\u8f93\u51fa"], "paste cells below": ["\u7c98\u8d34\u5230\u4e0b\u9762"], "Edit Notebook Metadata": ["\u7f16\u8f91\u754c\u9762\u5143\u6570\u636e"], "Left": ["\u5de6"], "Restart and Run All Cells": ["\u91cd\u542f\u5e76\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "Autosave disabled": ["\u81ea\u52a8\u4fdd\u5b58\u5931\u8d25"], "Dead kernel": ["\u6302\u6389\u7684\u670d\u52a1"], "Warning: too many matches (%d). Some changes might not be shown or applied.": ["\u8b66\u544a:\u592a\u591a\u7684\u5339\u914d(%d). \u6709\u4e9b\u66f4\u6539\u53ef\u80fd\u4e0d\u4f1a\u88ab\u663e\u793a\u6216\u5e94\u7528."], "Close the pager": ["\u5173\u95ed\u9875\u9762"], "hide the header": ["\u9690\u85cf\u6807\u9898"], "Rename Failed": ["\u91cd\u547d\u540d\u5931\u8d25"], "Saving notebook": ["\u4fdd\u5b58\u4ee3\u7801"], "Edit Mode (press %s to enable)": ["\u7f16\u8f91\u6a21\u5f0f(\u6309 %s \u751f\u6548)"], "Edit Cell Metadata": ["\u7f16\u8f91\u5757\u5143\u6570\u636e"], "select previous cell": ["\u9009\u62e9\u4e0a\u4e00\u4e2a\u4ee3\u7801\u5757"], "Enter a new name:": ["\u8bf7\u8f93\u5165\u65b0\u540d\u5b57:"], "find and replace": ["\u67e5\u627e\u5e76\u4e14\u66ff\u6362"], "Notes": ["\u4ee3\u7801"], "Unrecognized cell type": ["\u672a\u77e5\u7684\u5355\u5143\u683c\u7c7b\u578b"], "click to scroll output; double click to hide": ["\u70b9\u51fb\u6eda\u52a8\u8f93\u51fa;\u53cc\u51fb\u9690\u85cf"], "OK": ["\u786e\u5b9a"], "switch between showing and hiding the header": ["\u663e\u793a\u548c\u9690\u85cf\u6807\u9898\u4e4b\u95f4\u7684\u5207\u6362"], "confirm restart kernel and clear output": ["\u786e\u8ba4\u91cd\u542f\u670d\u52a1\u5e76\u4e14\u6e05\u7a7a\u8f93\u51fa"], "Not Connected": ["\u672a\u8fde\u63a5\u6210\u529f"], "redo selection": ["\u91cd\u65b0\u9009\u62e9"], "Running": ["\u8fd0\u884c"], "Kernel Idle": ["\u670d\u52a1\u7a7a\u95f2"], "Notification Area": ["\u4efb\u52a1\u680f\u901a\u77e5\u533a"], "You are using Jupyter notebook.": ["\u4f60\u6b63\u5728\u8fd0\u884cnotebook."], "Cannot find sys_info!": ["\u627e\u4e0d\u5230sys_info!"], "An error occurred while duplicating \"%s\".": ["\u5f53\u590d\u5236\"%s\" \u65f6\u51fa\u73b0\u9519\u8bef."], "Move an Item": ["\u79fb\u52a8\u4e00\u4e2a\u4ee3\u7801\u6587\u4ef6", "\u79fb\u52a8 %d \u4e2a\u4ee3\u7801\u6587\u4ef6"], "Are you sure you want to revert the notebook to the latest checkpoint?": ["\u786e\u5b9a\u64a4\u9500\u64cd\u4f5c?"], "delete line left of cursor": ["\u5220\u9664\u5149\u6807\u5de6\u8fb9\u7ebf"], "Fragment": ["\u788e\u7247"], "Could not find a kernel matching %s. Please select a kernel:": ["\u627e\u4e0d\u5230\u670d\u52a1\u5339\u914d %s. \u8bf7\u9009\u62e9\u4e00\u4e2a\u670d\u52a1:"], "change cell to heading 5": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 5"], "click to expand output; double click to hide output": ["\u70b9\u51fb\u5c55\u5f00\u8f93\u51fa; \u53cc\u51fb\u9690\u85cf"], "Invalid notebook name. Notebook names must have 1 or more characters and can contain any characters except :/\\. Please enter a new notebook name:": ["\u65e0\u6548\u7684\u6587\u4ef6\u540d. \u4ee3\u7801\u540d\u4e0d\u80fd\u4e3a\u7a7a \u5e76\u4e14\u4e0d\u80fd\u5305\u542b\".\" \u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u6587\u4ef6\u540d:"], "An error occurred while creating a new file.": ["\u521b\u5efa\u65b0\u6587\u4ef6\u7684\u65f6\u5019\u51fa\u73b0\u4e86\u4e00\u4e2a\u9519\u8bef"], "Checkpoint deleted": ["checkpoint\u5df2\u5220\u9664"], "WARNING: Could not save invalid JSON.": ["\u8b66\u544a: \u4e0d\u80fd\u4fdd\u5b58\u65e0\u6548\u7684JSON."], "Pressing <code>Enter</code> or clicking in the input text area of the cell switches to Edit Mode.": ["\u6309\u4e0b<code>Enter</code>, \u6216\u8005\u70b9\u51fb\u8f93\u5165\u6587\u672c\u533a\u57df, \u5c06\u4f60\u8fd4\u56de\u5230\u547d\u4ee4\u6a21\u5f0f. "], "toggle all cells output scrolled": ["\u5207\u6362\u6240\u6709\u5355\u5143\u683c\u7684\u8f93\u51fa"], "Continue Without Kernel": ["\u7ee7\u7eed\u8fd0\u884c\u6ca1\u6709\u670d\u52a1"], "A connection to the notebook server could not be established. The notebook will continue trying to reconnect. Check your network connection or notebook server configuration.": ["\u5230\u540e\u53f0\u670d\u52a1\u7684\u8fde\u63a5\u6ca1\u80fd\u5efa\u7acb, \u6211\u4eec\u4f1a\u7ee7\u7eed\u5c1d\u8bd5\u91cd\u8fde, \u8bf7\u68c0\u51fa\u7f51\u7edc\u8fde\u63a5...\u8fd8\u6709\u670d\u52a1\u914d\u7f6e."], "Server error: ": ["\u670d\u52a1\u51fa\u73b0\u9519\u8bef:"], "show keyboard shortcuts": ["\u663e\u793a\u5feb\u6377\u952e"], "Out[%d]:": ["\u8f93\u51fa[%d]:"], "Cmd-V": [""], "End": ["End"], "move cursor down": ["\u5149\u6807\u4e0b\u79fb"], "Restart": ["\u91cd\u542f"], "Edit": ["\u7f16\u8f91"], "Raw Cell MIME Type": [""], "Manually edit the JSON below to manipulate the metadata for this cell.": ["\u624b\u52a8\u7f16\u8f91\u4e0b\u9762\u7684JSON\u4ee3\u7801\u6765\u4fee\u6539\u5757\u5143\u6570\u636e."], "change cell to heading 1": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 1"], "Esc": ["Esc"], "change cell to raw": ["\u6e05\u9664\u4ee3\u7801\u5757\u683c\u5f0f"], "To preserve the original version, close the notebook without saving it.": ["\u4e3a\u4e86\u4fdd\u5b58\u539f\u59cb\u7248\u672c, \u5173\u95ed\u7b14\u8bb0\u672c\u800c\u4e0d\u4fdd\u5b58\u5b83."], "code completion or indent": ["\u4ee3\u7801\u5b8c\u6210\u6216\u7f29\u8fdb"], "Ctrl-V": [""], "Press %s again to paste": ["\u518d\u6309\u4e00\u6b21 %s \u7c98\u8d34"], "move cursor up": ["\u5149\u6807\u4e0a\u79fb"], "An unknown error occurred while loading this notebook. This version can load notebook formats %s or earlier. See the server log for details.": ["\u52a0\u8f7d\u672c\u7b14\u8bb0\u672c\u65f6\u51fa\u73b0\u4e86\u4e00\u4e2a\u672a\u77e5\u7684\u9519\u8bef. \u8fd9\u4e2a\u7248\u672c\u53ef\u4ee5\u52a0\u8f7d%s\u6216\u66f4\u65e9\u7684\u7b14\u8bb0\u672c. \u6709\u5173\u8be6\u7ec6\u4fe1\u606f, \u8bf7\u53c2\u9605\u670d\u52a1\u5668\u65e5\u5fd7."], "Space": ["\u7a7a\u683c"], "Jupyter no longer uses special heading cells. Instead, write your headings in Markdown cells using # characters:": ["Jupyter\u4e0d\u518d\u4f7f\u7528\u7279\u6b8a\u7684\u6807\u9898\u5355\u5143\u683c. \u76f8\u53cd, \u5728Markdown\u5355\u5143\u4e2d\u4f7f\u7528\u5b57\u7b26\u6765\u5199\u6807\u9898:"], "Write raw LaTeX or other formats here, for use with nbconvert. It will not be rendered in the notebook. When passing through nbconvert, a Raw Cell's content is added to the output unmodified.": [""], "change cell to heading 6": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 6"], "Trust this notebook?": ["\u4fe1\u4efb\u8fd9\u4e2a\u4ee3\u7801?"], "cut cell attachments": ["\u526a\u5207\u4ee3\u7801\u5757"], "Raw Cell Format": [""], "Backspace": ["\u5220\u9664"], "Set the MIME type of the raw cell:": [""], "toggles line numbers in all cells, and persist the setting": ["\u5728\u6240\u6709\u5355\u5143\u683c\u4e2d\u5207\u6362\u884c\u53f7\uff0c\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "Raw NBConvert Format": [""], "toggle all cells output collapsed": ["\u5207\u6362\u6240\u6709\u5355\u5143\u683c\u7684\u8f93\u51fa"], "Filename": ["\u6587\u4ef6\u540d"], "Could not access sys_info variable for version information.": ["\u65e0\u6cd5\u4e3a\u7248\u672c\u4fe1\u606f\u8bbf\u95eesysinfo\u53d8\u91cf."], "run cell, select below": ["\u8fd0\u884c\u4ee3\u7801\u5757, \u9009\u62e9\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "clear output of selected cells": ["\u6e05\u7a7a\u5df2\u9009\u62e9\u5355\u5143\u683c\u7684\u8f93\u51fa"], "An error occurred while creating a new folder.": ["\u521b\u5efa\u65b0\u6587\u4ef6\u5939\u7684\u65f6\u5019\u51fa\u73b0\u4e86\u4e00\u4e2a\u9519\u8bef."], "See your browser Javascript console for more details.": ["\u66f4\u591a\u7ec6\u8282\u8bf7\u53c2\u89c1\u60a8\u7684\u6d4f\u89c8\u5668Javascript\u63a7\u5236\u53f0\u3002"], "Rename notebook": ["\u91cd\u547d\u540d"], "Clipboard types: %s": ["\u526a\u8d34\u677f\u7c7b\u578b: %s"], "click to reconnect": ["\u70b9\u51fb\u91cd\u8fde"], "Notebook validation failed": ["Notebook \u5931\u6548"], "<b>Command mode</b> binds the keyboard to notebook level commands and is indicated by a grey cell border with a blue left margin.": ["<b>\u547d\u4ee4\u6a21\u5f0f</b>\u5c06\u952e\u76d8\u4e0e\u7b14\u8bb0\u672c\u7ea7\u547d\u4ee4\u7ed1\u5b9a\u5728\u4e00\u8d77\uff0c\u5e76\u901a\u8fc7\u4e00\u4e2a\u7070\u8272\u7684\u5355\u5143\u683c\u8fb9\u754c\u663e\u793a\uff0c\u8be5\u8fb9\u6846\u4e3a\u84dd\u8272\u7684\u5de6\u8fb9\u6846\u3002"], "go one word right": ["\u8df3\u5230\u5355\u8bcd\u53f3\u8fb9"], "This is the Kernel indicator. It looks like this when the Kernel is idle.": ["\u8fd9\u662f\u5185\u6838\u6307\u793a\u5668\u3002\u5f53\u5185\u6838\u7a7a\u95f2\u65f6\uff0c\u5b83\u770b\u8d77\u6765\u5c31\u50cf\u8fd9\u6837\u3002"], "Delete Failed": ["\u5220\u9664\u5931\u8d25"], "Save and Checkpoint": ["\u4fdd\u5b58\u5e76\u68c0\u67e5"], "change cell to heading 3": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210heading 3"], "Replace": ["\u66ff\u6362"], "Notebook save failed": ["\u4ee3\u7801\u4fdd\u5b58\u5931\u8d25"], "Try Restarting Now": ["\u73b0\u5728\u5c1d\u8bd5\u91cd\u542f"], "Down": ["\u4e0b"], "The Notebook has two modes: Edit Mode and Command Mode. In this area, an indicator can appear to tell you which mode you are in.": ["\u8be5\u7b14\u8bb0\u672c\u6709\u4e24\u79cd\u6a21\u5f0f:\u7f16\u8f91\u6a21\u5f0f\u548c\u547d\u4ee4\u6a21\u5f0f. \u5728\u8fd9\u4e2a\u533a\u57df, \u4e00\u4e2a\u6307\u793a\u5668\u53ef\u4ee5\u663e\u793a\u4f60\u5728\u54ea\u4e2a\u6a21\u5f0f. "], "Run": ["\u8fd0\u884c"], "merge cell with previous cell": ["\u5408\u5e76\u4e0a\u4e00\u4e2a\u5355\u5143\u683c"], "Raw NBConvert": ["\u539f\u751f NBConvert"], "Click here to change the filename for this notebook.": ["\u70b9\u51fb\u6539\u53d8\u4ee3\u7801\u6587\u4ef6\u540d"], "switch between showing and hiding the toolbar": ["\u9009\u62e9\u663e\u793a/\u9690\u85cf\u5de5\u5177\u680f"], "Edit the list of tags below. All whitespace is treated as tag separators.": ["\u7f16\u8f91\u4e0b\u9762\u7684\u6807\u7b7e\u5217\u8868. \u6240\u6709\u7a7a\u683c\u90fd\u88ab\u5f53\u4f5c\u6807\u8bb0\u5206\u9694\u7b26."], "scroll cell top": ["\u6eda\u52a8\u5230\u5355\u5143\u683c\u5f00\u59cb\u5904"], "Cannot upload invalid Notebook": ["\u65e0\u6cd5\u4e0a\u4f20\u65e0\u6548\u7684Notebook"], "Unrecognized cell type: %s": ["\u672a\u77e5\u7684\u5355\u5143\u683c\u7c7b\u578b: %s"], "show command pallette": ["\u663e\u793a\u547d\u4ee4\u914d\u7f6e"], "unable to contact kernel": ["\u4e0d\u80fd\u8fde\u63a5\u5230\u670d\u52a1"]}}, "domain": "nbjs"};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

</head>

<body class="edit_app "
 
data-base-url="/"
data-file-path="data_cervical/pytorch_running/third/slim_zye/qt/torchself/qttorch1.py"

  
 

dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook需要的JavaScript.<br>
      请允许它继续.
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="/tree" title='指示板'>
      <img src='/static/base/images/logo.png?v=641991992878ee24c6f3826e81054a0f' alt='Jupyter Notebook'/>
  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename"></span>
    <span class="last_modified"></span>
</span>


  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">注销</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p  class="navbar-text indicator_area">
          <span id="current-mode" >当前模式</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">文件</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="#">新建</a></li>
                <li id="save-file"><a href="#">保存</a></li>
                <li id="rename-file"><a href="#">重命名</a></li>
                <li id="download-file"><a href="#">下载</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">编辑</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="#">查找</a></li>
                <li id="menu-replace"><a href="#">查找 &amp; 替换</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">键值对</li>
                <li id="menu-keymap-default"><a href="#">默认<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="#">代码编辑器<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">查看</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="显示/隐藏 标题和logo">
              <a href="#">切换Header</a></li>
              <li id="menu-line-numbers"><a href="#">切换行号</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">语言</a>
              <ul id="mode-menu" class="dropdown-menu">
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"></div>
</div>


</div>






    


<script src="/static/edit/js/main.min.js?v=8953b35ff72d1380d055f1668327fe2e" type="text/javascript" charset="utf-8"></script>


<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>