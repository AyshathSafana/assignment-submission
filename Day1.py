<!DOCTYPE html>
<!-- saved from url=(0045)http://localhost:8888/notebooks/Desktop.ipynb -->
<html lang="en-gb"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Desktop - Jupyter Notebook</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./Desktop - Jupyter Notebook_files/MathJax.js" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distinguish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/codemirror.css">


    <link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8888/notebooks/Desktop.ipynb" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./Desktop - Jupyter Notebook_files/custom.css" type="text/css">
    <script src="./Desktop - Jupyter Notebook_files/promise.min.js" type="text/javascript" charset="utf-8"></script>
    <script src="./Desktop - Jupyter Notebook_files/react.production.min.js" type="text/javascript"></script>
    <script src="./Desktop - Jupyter Notebook_files/react-dom.production.min.js" type="text/javascript"></script>
    <script src="./Desktop - Jupyter Notebook_files/index.js" type="text/javascript"></script>
    <script src="./Desktop - Jupyter Notebook_files/require.js" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20210921123720",
          
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

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./Desktop - Jupyter Notebook_files/contents.js"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 5px 0px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 5px; -webkit-border-radius: 5px; -moz-border-radius: 5px; -khtml-border-radius: 5px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 1px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: .7em}
.MathJax_MenuRadioCheck.RTL {right: .7em; left: auto}
.MathJax_MenuLabel {padding: 1px 2em 3px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #DDDDDD; margin: 4px 3px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: #606872; color: white}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888; display: contents}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./Desktop - Jupyter Notebook_files/custom.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/plotlywidget/extension" src="./Desktop - Jupyter Notebook_files/extension.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./Desktop - Jupyter Notebook_files/extension(1).js"></script><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */
.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */
.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


.p-Widget.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-CommandPalette-search {
  flex: 0 0 auto;
}


.p-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


.p-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


.p-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


.p-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


.p-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


.p-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


.p-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-DockPanel {
  z-index: 0;
}


.p-DockPanel-widget {
  z-index: 0;
}


.p-DockPanel-tabBar {
  z-index: 1;
}


.p-DockPanel-handle {
  z-index: 2;
}


.p-DockPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


.p-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


.p-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


.p-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


.p-DockPanel-overlay.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


.p-Menu-item {
  display: table-row;
}


.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed {
  display: none !important;
}


.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


.p-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


.p-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


.p-MenuBar-item {
  box-sizing: border-box;
}


.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel {
  display: inline-block;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


.p-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


.p-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-SplitPanel-child {
  z-index: 0;
}


.p-SplitPanel-handle {
  z-index: 1;
}


.p-SplitPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle {
  cursor: ew-resize;
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle {
  cursor: ns-resize;
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabPanel-tabBar {
  z-index: 1;
}


.p-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\f127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    align-self: flex-start;
}
</style><style type="text/css">/**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
:root {
  --md-red-50: #FFEBEE;
  --md-red-100: #FFCDD2;
  --md-red-200: #EF9A9A;
  --md-red-300: #E57373;
  --md-red-400: #EF5350;
  --md-red-500: #F44336;
  --md-red-600: #E53935;
  --md-red-700: #D32F2F;
  --md-red-800: #C62828;
  --md-red-900: #B71C1C;
  --md-red-A100: #FF8A80;
  --md-red-A200: #FF5252;
  --md-red-A400: #FF1744;
  --md-red-A700: #D50000;

  --md-pink-50: #FCE4EC;
  --md-pink-100: #F8BBD0;
  --md-pink-200: #F48FB1;
  --md-pink-300: #F06292;
  --md-pink-400: #EC407A;
  --md-pink-500: #E91E63;
  --md-pink-600: #D81B60;
  --md-pink-700: #C2185B;
  --md-pink-800: #AD1457;
  --md-pink-900: #880E4F;
  --md-pink-A100: #FF80AB;
  --md-pink-A200: #FF4081;
  --md-pink-A400: #F50057;
  --md-pink-A700: #C51162;

  --md-purple-50: #F3E5F5;
  --md-purple-100: #E1BEE7;
  --md-purple-200: #CE93D8;
  --md-purple-300: #BA68C8;
  --md-purple-400: #AB47BC;
  --md-purple-500: #9C27B0;
  --md-purple-600: #8E24AA;
  --md-purple-700: #7B1FA2;
  --md-purple-800: #6A1B9A;
  --md-purple-900: #4A148C;
  --md-purple-A100: #EA80FC;
  --md-purple-A200: #E040FB;
  --md-purple-A400: #D500F9;
  --md-purple-A700: #AA00FF;

  --md-deep-purple-50: #EDE7F6;
  --md-deep-purple-100: #D1C4E9;
  --md-deep-purple-200: #B39DDB;
  --md-deep-purple-300: #9575CD;
  --md-deep-purple-400: #7E57C2;
  --md-deep-purple-500: #673AB7;
  --md-deep-purple-600: #5E35B1;
  --md-deep-purple-700: #512DA8;
  --md-deep-purple-800: #4527A0;
  --md-deep-purple-900: #311B92;
  --md-deep-purple-A100: #B388FF;
  --md-deep-purple-A200: #7C4DFF;
  --md-deep-purple-A400: #651FFF;
  --md-deep-purple-A700: #6200EA;

  --md-indigo-50: #E8EAF6;
  --md-indigo-100: #C5CAE9;
  --md-indigo-200: #9FA8DA;
  --md-indigo-300: #7986CB;
  --md-indigo-400: #5C6BC0;
  --md-indigo-500: #3F51B5;
  --md-indigo-600: #3949AB;
  --md-indigo-700: #303F9F;
  --md-indigo-800: #283593;
  --md-indigo-900: #1A237E;
  --md-indigo-A100: #8C9EFF;
  --md-indigo-A200: #536DFE;
  --md-indigo-A400: #3D5AFE;
  --md-indigo-A700: #304FFE;

  --md-blue-50: #E3F2FD;
  --md-blue-100: #BBDEFB;
  --md-blue-200: #90CAF9;
  --md-blue-300: #64B5F6;
  --md-blue-400: #42A5F5;
  --md-blue-500: #2196F3;
  --md-blue-600: #1E88E5;
  --md-blue-700: #1976D2;
  --md-blue-800: #1565C0;
  --md-blue-900: #0D47A1;
  --md-blue-A100: #82B1FF;
  --md-blue-A200: #448AFF;
  --md-blue-A400: #2979FF;
  --md-blue-A700: #2962FF;

  --md-light-blue-50: #E1F5FE;
  --md-light-blue-100: #B3E5FC;
  --md-light-blue-200: #81D4FA;
  --md-light-blue-300: #4FC3F7;
  --md-light-blue-400: #29B6F6;
  --md-light-blue-500: #03A9F4;
  --md-light-blue-600: #039BE5;
  --md-light-blue-700: #0288D1;
  --md-light-blue-800: #0277BD;
  --md-light-blue-900: #01579B;
  --md-light-blue-A100: #80D8FF;
  --md-light-blue-A200: #40C4FF;
  --md-light-blue-A400: #00B0FF;
  --md-light-blue-A700: #0091EA;

  --md-cyan-50: #E0F7FA;
  --md-cyan-100: #B2EBF2;
  --md-cyan-200: #80DEEA;
  --md-cyan-300: #4DD0E1;
  --md-cyan-400: #26C6DA;
  --md-cyan-500: #00BCD4;
  --md-cyan-600: #00ACC1;
  --md-cyan-700: #0097A7;
  --md-cyan-800: #00838F;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84FFFF;
  --md-cyan-A200: #18FFFF;
  --md-cyan-A400: #00E5FF;
  --md-cyan-A700: #00B8D4;

  --md-teal-50: #E0F2F1;
  --md-teal-100: #B2DFDB;
  --md-teal-200: #80CBC4;
  --md-teal-300: #4DB6AC;
  --md-teal-400: #26A69A;
  --md-teal-500: #009688;
  --md-teal-600: #00897B;
  --md-teal-700: #00796B;
  --md-teal-800: #00695C;
  --md-teal-900: #004D40;
  --md-teal-A100: #A7FFEB;
  --md-teal-A200: #64FFDA;
  --md-teal-A400: #1DE9B6;
  --md-teal-A700: #00BFA5;

  --md-green-50: #E8F5E9;
  --md-green-100: #C8E6C9;
  --md-green-200: #A5D6A7;
  --md-green-300: #81C784;
  --md-green-400: #66BB6A;
  --md-green-500: #4CAF50;
  --md-green-600: #43A047;
  --md-green-700: #388E3C;
  --md-green-800: #2E7D32;
  --md-green-900: #1B5E20;
  --md-green-A100: #B9F6CA;
  --md-green-A200: #69F0AE;
  --md-green-A400: #00E676;
  --md-green-A700: #00C853;

  --md-light-green-50: #F1F8E9;
  --md-light-green-100: #DCEDC8;
  --md-light-green-200: #C5E1A5;
  --md-light-green-300: #AED581;
  --md-light-green-400: #9CCC65;
  --md-light-green-500: #8BC34A;
  --md-light-green-600: #7CB342;
  --md-light-green-700: #689F38;
  --md-light-green-800: #558B2F;
  --md-light-green-900: #33691E;
  --md-light-green-A100: #CCFF90;
  --md-light-green-A200: #B2FF59;
  --md-light-green-A400: #76FF03;
  --md-light-green-A700: #64DD17;

  --md-lime-50: #F9FBE7;
  --md-lime-100: #F0F4C3;
  --md-lime-200: #E6EE9C;
  --md-lime-300: #DCE775;
  --md-lime-400: #D4E157;
  --md-lime-500: #CDDC39;
  --md-lime-600: #C0CA33;
  --md-lime-700: #AFB42B;
  --md-lime-800: #9E9D24;
  --md-lime-900: #827717;
  --md-lime-A100: #F4FF81;
  --md-lime-A200: #EEFF41;
  --md-lime-A400: #C6FF00;
  --md-lime-A700: #AEEA00;

  --md-yellow-50: #FFFDE7;
  --md-yellow-100: #FFF9C4;
  --md-yellow-200: #FFF59D;
  --md-yellow-300: #FFF176;
  --md-yellow-400: #FFEE58;
  --md-yellow-500: #FFEB3B;
  --md-yellow-600: #FDD835;
  --md-yellow-700: #FBC02D;
  --md-yellow-800: #F9A825;
  --md-yellow-900: #F57F17;
  --md-yellow-A100: #FFFF8D;
  --md-yellow-A200: #FFFF00;
  --md-yellow-A400: #FFEA00;
  --md-yellow-A700: #FFD600;

  --md-amber-50: #FFF8E1;
  --md-amber-100: #FFECB3;
  --md-amber-200: #FFE082;
  --md-amber-300: #FFD54F;
  --md-amber-400: #FFCA28;
  --md-amber-500: #FFC107;
  --md-amber-600: #FFB300;
  --md-amber-700: #FFA000;
  --md-amber-800: #FF8F00;
  --md-amber-900: #FF6F00;
  --md-amber-A100: #FFE57F;
  --md-amber-A200: #FFD740;
  --md-amber-A400: #FFC400;
  --md-amber-A700: #FFAB00;

  --md-orange-50: #FFF3E0;
  --md-orange-100: #FFE0B2;
  --md-orange-200: #FFCC80;
  --md-orange-300: #FFB74D;
  --md-orange-400: #FFA726;
  --md-orange-500: #FF9800;
  --md-orange-600: #FB8C00;
  --md-orange-700: #F57C00;
  --md-orange-800: #EF6C00;
  --md-orange-900: #E65100;
  --md-orange-A100: #FFD180;
  --md-orange-A200: #FFAB40;
  --md-orange-A400: #FF9100;
  --md-orange-A700: #FF6D00;

  --md-deep-orange-50: #FBE9E7;
  --md-deep-orange-100: #FFCCBC;
  --md-deep-orange-200: #FFAB91;
  --md-deep-orange-300: #FF8A65;
  --md-deep-orange-400: #FF7043;
  --md-deep-orange-500: #FF5722;
  --md-deep-orange-600: #F4511E;
  --md-deep-orange-700: #E64A19;
  --md-deep-orange-800: #D84315;
  --md-deep-orange-900: #BF360C;
  --md-deep-orange-A100: #FF9E80;
  --md-deep-orange-A200: #FF6E40;
  --md-deep-orange-A400: #FF3D00;
  --md-deep-orange-A700: #DD2C00;

  --md-brown-50: #EFEBE9;
  --md-brown-100: #D7CCC8;
  --md-brown-200: #BCAAA4;
  --md-brown-300: #A1887F;
  --md-brown-400: #8D6E63;
  --md-brown-500: #795548;
  --md-brown-600: #6D4C41;
  --md-brown-700: #5D4037;
  --md-brown-800: #4E342E;
  --md-brown-900: #3E2723;

  --md-grey-50: #FAFAFA;
  --md-grey-100: #F5F5F5;
  --md-grey-200: #EEEEEE;
  --md-grey-300: #E0E0E0;
  --md-grey-400: #BDBDBD;
  --md-grey-500: #9E9E9E;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #ECEFF1;
  --md-blue-grey-100: #CFD8DC;
  --md-blue-grey-200: #B0BEC5;
  --md-blue-grey-300: #90A4AE;
  --md-blue-grey-400: #78909C;
  --md-blue-grey-500: #607D8B;
  --md-blue-grey-600: #546E7A;
  --md-blue-grey-700: #455A64;
  --md-blue-grey-800: #37474F;
  --md-blue-grey-900: #263238;
}</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/


/*
 * Optional monospace font for input/output prompt.
 */
 /* Commented out in ipywidgets since we don't need it. */
/* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

/*
 * Added for compabitility with output area
 */
:root {
  --jp-icon-search: none;
  --jp-ui-select-caret: none;
}


:root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-700);
  --jp-border-color1: var(--md-grey-500);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-100);

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));
  --jp-ui-icon-font-size: 14px; /* Ensures px perfect FontAwesome icons */
  --jp-ui-font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  --jp-ui-font-color0: rgba(0,0,0,1.0);
  --jp-ui-font-color1: rgba(0,0,0,0.8);
  --jp-ui-font-color2: rgba(0,0,0,0.5);
  --jp-ui-font-color3: rgba(0,0,0,0.3);

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  --jp-inverse-ui-font-color0: rgba(255,255,255,1);
  --jp-inverse-ui-font-color1: rgba(255,255,255,1.0);
  --jp-inverse-ui-font-color2: rgba(255,255,255,0.7);
  --jp-inverse-ui-font-color3: rgba(255,255,255,0.5);

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */

  --jp-content-font-size: 13px;
  --jp-content-line-height: 1.5;
  --jp-content-font-color0: black;
  --jp-content-font-color1: black;
  --jp-content-font-color2: var(--md-grey-700);
  --jp-content-font-color3: var(--md-grey-500);

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.307;
  --jp-code-padding: 5px;
  --jp-code-font-family: monospace;


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-700);
  --jp-brand-color1: var(--md-blue-500);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);

  --jp-accent-color0: var(--md-green-700);
  --jp-accent-color1: var(--md-green-500);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-700);
  --jp-warn-color1: var(--md-orange-500);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-700);
  --jp-error-color1: var(--md-red-500);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-700);
  --jp-success-color1: var(--md-green-500);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-700);
  --jp-info-color1: var(--md-cyan-500);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-editor-background: #f7f7f7;
  --jp-cell-editor-border-color: #cfcfcf;
  --jp-cell-editor-background-edit: var(--jp-ui-layout-color1);
  --jp-cell-editor-border-color-edit: var(--jp-brand-color1);
  --jp-cell-prompt-width: 100px;
  --jp-cell-prompt-font-family: 'Roboto Mono', monospace;
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1.0;
  --jp-cell-prompt-opacity-not-active: 0.4;
  --jp-cell-prompt-font-color-not-active: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307FC1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #BF5B3D;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-scroll-padding: 100px;

  /* Console specific styles */

  --jp-console-background: var(--md-grey-100);

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--md-grey-400);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color0);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);
}
</style><style type="text/css">/* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

/*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

.jupyter-widgets.widget-tab > .p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}

/* End tabbar.css */
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

:root {
    --jp-widgets-color: var(--jp-content-font-color1);
    --jp-widgets-label-color: var(--jp-widgets-color);
    --jp-widgets-readout-color: var(--jp-widgets-color);
    --jp-widgets-font-size: var(--jp-ui-font-size1);
    --jp-widgets-margin: 2px;
    --jp-widgets-inline-height: 28px;
    --jp-widgets-inline-width: 300px;
    --jp-widgets-inline-width-short: calc(var(--jp-widgets-inline-width) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-width-tiny: calc(var(--jp-widgets-inline-width-short) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-margin: 4px; /* margin between inline elements */
    --jp-widgets-inline-label-width: 80px;
    --jp-widgets-border-width: var(--jp-border-width);
    --jp-widgets-vertical-height: 200px;
    --jp-widgets-horizontal-tab-height: 24px;
    --jp-widgets-horizontal-tab-width: 144px;
    --jp-widgets-horizontal-tab-top-border: 2px;
    --jp-widgets-progress-thickness: 20px;
    --jp-widgets-container-padding: 15px;
    --jp-widgets-input-padding: 4px;
    --jp-widgets-radio-item-height-adjustment: 8px;
    --jp-widgets-radio-item-height: calc(var(--jp-widgets-inline-height) - var(--jp-widgets-radio-item-height-adjustment));
    --jp-widgets-slider-track-thickness: 4px;
    --jp-widgets-slider-border-width: var(--jp-widgets-border-width);
    --jp-widgets-slider-handle-size: 16px;
    --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
    --jp-widgets-slider-handle-background-color: var(--jp-layout-color1);
    --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
    --jp-widgets-menu-item-height: 24px;
    --jp-widgets-dropdown-arrow: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
    --jp-widgets-input-color: var(--jp-ui-font-color1);
    --jp-widgets-input-background-color: var(--jp-layout-color1);
    --jp-widgets-input-border-color: var(--jp-border-color1);
    --jp-widgets-input-focus-border-color: var(--jp-brand-color2);
    --jp-widgets-input-border-width: var(--jp-widgets-border-width);
    --jp-widgets-disabled-opacity: 0.6;

    /* From Material Design Lite */
    --md-shadow-key-umbra-opacity: 0.2;
    --md-shadow-key-penumbra-opacity: 0.14;
    --md-shadow-ambient-shadow-opacity: 0.12;
}

.jupyter-widgets {
    margin: var(--jp-widgets-margin);
    box-sizing: border-box;
    color: var(--jp-widgets-color);
    overflow: visible;
}

.jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
}

.jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

/* vbox and hbox */

.widget-inline-hbox {
    /* Horizontal widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: baseline;
}

.widget-inline-vbox {
    /* Vertical Widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.widget-box {
    box-sizing: border-box;
    display: flex;
    margin: 0;
    overflow: auto;
}

.widget-gridbox {
    box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

.widget-hbox {
    flex-direction: row;
}

.widget-vbox {
    flex-direction: column;
}

/* General Button Styling */

.jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: var(--jp-widgets-font-size);
    cursor: pointer;

    height: var(--jp-widgets-inline-height);
    border: 0px solid;
    line-height: var(--jp-widgets-inline-height);
    box-shadow: none;

    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color2);
    border-color: var(--jp-border-color2);
    border: none;
    user-select: none;
}

.jupyter-button i.fa {
    margin-right: var(--jp-widgets-inline-margin);
    pointer-events: none;
}

.jupyter-button:empty:before {
    content: "\200b"; /* zero-width space */
}

.jupyter-widgets.jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.jupyter-button i.fa.center {
    margin-right: 0;
}

.jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 3px 1px -2px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity)),
                0 1px 5px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity));
}

.jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
                0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color3);
}

.jupyter-button:focus:enabled {
    outline: 1px solid var(--jp-widgets-input-focus-border-color);
}

/* Button "Primary" Styling */

.jupyter-button.mod-primary {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-brand-color1);
}

.jupyter-button.mod-primary.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

.jupyter-button.mod-primary:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

/* Button "Success" Styling */

.jupyter-button.mod-success {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-success-color1);
}

.jupyter-button.mod-success.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

.jupyter-button.mod-success:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

 /* Button "Info" Styling */

.jupyter-button.mod-info {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-info-color1);
}

.jupyter-button.mod-info.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

.jupyter-button.mod-info:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

/* Button "Warning" Styling */

.jupyter-button.mod-warning {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-warn-color1);
}

.jupyter-button.mod-warning.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

.jupyter-button.mod-warning:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

/* Button "Danger" Styling */

.jupyter-button.mod-danger {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-error-color1);
}

.jupyter-button.mod-danger.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

.jupyter-button.mod-danger:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

/* Widget Button, Widget Toggle Button, Widget Upload */

.widget-button, .widget-toggle-button, .widget-upload {
    width: var(--jp-widgets-inline-width-short);
}

/* Widget Label Styling */

/* Override Bootstrap label css */
.jupyter-widgets label {
    margin-bottom: initial;
}

.widget-label-basic {
    /* Basic Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-label {
    /* Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: right;
    margin-right: calc( var(--jp-widgets-inline-margin) * 2 );
    width: var(--jp-widgets-inline-label-width);
    flex-shrink: 0;
}

.widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: center;
    line-height: var(--jp-widgets-inline-height);
}

/* Widget Readout Styling */

.widget-readout {
    color: var(--jp-widgets-readout-color);
    font-size: var(--jp-widgets-font-size);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

.widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                        0 3px 1px -2px rgba(0, 0, 0, 0.14),
                        0 1px 5px 0 rgba(0, 0, 0, 0.12);

    -moz-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                     0 3px 1px -2px rgba(0, 0, 0, 0.14),
                     0 1px 5px 0 rgba(0, 0, 0, 0.12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                0 3px 1px -2px rgba(0, 0, 0, 0.14),
                0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: var(--jp-widgets-inline-width-short);
    min-width: var(--jp-widgets-inline-width-tiny);
    margin-left: var(--jp-widgets-inline-margin);
}

.widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: var(--jp-widgets-inline-margin);
    /* as wide as the widget */
    width: inherit;
}

/* Widget Checkbox Styling */

.widget-checkbox {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-checkbox input[type="checkbox"] {
    margin: 0px calc( var(--jp-widgets-inline-margin) * 2 ) 0px 0px;
    line-height: var(--jp-widgets-inline-height);
    font-size: large;
    flex-grow: 1;
    flex-shrink: 0;
    align-self: center;
}

/* Widget Valid Styling */

.widget-valid {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width-short);
    font-size: var(--jp-widgets-font-size);
}

.widget-valid i:before {
    line-height: var(--jp-widgets-inline-height);
    margin-right: var(--jp-widgets-inline-margin);
    margin-left: var(--jp-widgets-inline-margin);

    /* from the fa class in FontAwesome: https://github.com/FortAwesome/Font-Awesome/blob/49100c7c3a7b58d50baa71efef11af41a66b03d3/css/font-awesome.css#L14 */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.widget-valid.mod-valid i:before {
    content: "\f00c";
    color: green;
}

.widget-valid.mod-invalid i:before {
    content: "\f00d";
    color: red;
}

.widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

/* Widget Text and TextArea Stying */

.widget-textarea, .widget-text {
    width: var(--jp-widgets-inline-width);
}

.widget-text input[type="text"], .widget-text input[type="number"]{
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-textarea textarea:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.widget-text input[type="text"], .widget-text input[type="number"], .widget-textarea textarea {
    box-sizing: border-box;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    outline: none !important;
}
    
.widget-text input[type="text"], .widget-textarea textarea {
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2);
}

.widget-text input[type="number"] {
    padding: var(--jp-widgets-input-padding) 0 var(--jp-widgets-input-padding) calc(var(--jp-widgets-input-padding) *  2);
}

.widget-textarea textarea {
    height: inherit;
    width: inherit;
}

.widget-text input:focus, .widget-textarea textarea:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

/* Widget Slider */

.widget-slider .ui-slider {
    /* Slider Track */
    border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
    background: var(--jp-layout-color3);
    box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

.widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: var(--jp-widgets-slider-handle-background-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-handle-border-color);
    box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

/* Override jquery-ui */
.widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
}

.widget-slider .ui-slider .ui-slider-handle:active {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border-color: var(--jp-widgets-slider-active-handle-color);
    z-index: 2;
    transform: scale(1.2);
}

.widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: var(--jp-widgets-slider-active-handle-color);
    z-index: 0;
}

/* Shapes of Slider Handles */

.widget-hslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    margin-left: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    top: 0;
}

.widget-vslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    left: 0;
}

.widget-hslider .ui-slider .ui-slider-range {
    height: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

.widget-vslider .ui-slider .ui-slider-range {
    width: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

/* Horizontal Slider */

.widget-hslider {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    align-items: center;
}

.widgets-slider .slider-container {
    overflow: visible;
}

.widget-hslider .slider-container {
    height: var(--jp-widgets-inline-height);
    margin-left: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-right: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    flex: 1 1 var(--jp-widgets-inline-width-short);
}

.widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: var(--jp-widgets-slider-track-thickness);
    margin-top: calc((var(--jp-widgets-inline-height) - var(--jp-widgets-slider-track-thickness)) / 2);
    width: 100%;
}

/* Vertical Slider */

.widget-vbox .widget-label {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-vslider {
    /* Vertical Slider */
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vslider .slider-container {
    flex: 1 1 var(--jp-widgets-inline-width-short);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-top: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    display: flex;
    flex-direction: column;
}

.widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: var(--jp-widgets-slider-track-thickness);
    flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

/* Widget Progress Styling */

.progress-bar {
    -webkit-transition: none;
    -moz-transition: none;
    -ms-transition: none;
    -o-transition: none;
    transition: none;
}

.progress-bar {
    height: var(--jp-widgets-inline-height);
}

.progress-bar {
    background-color: var(--jp-brand-color1);
}

.progress-bar-success {
    background-color: var(--jp-success-color1);
}

.progress-bar-info {
    background-color: var(--jp-info-color1);
}

.progress-bar-warning {
    background-color: var(--jp-warn-color1);
}

.progress-bar-danger {
    background-color: var(--jp-error-color1);
}

.progress {
    background-color: var(--jp-layout-color2);
    border: none;
    box-shadow: none;
}

/* Horisontal Progress */

.widget-hprogress {
    /* Progress Bar */
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    align-items: center;

}

.widget-hprogress .progress {
    flex-grow: 1;
    margin-top: var(--jp-widgets-input-padding);
    margin-bottom: var(--jp-widgets-input-padding);
    align-self: stretch;
    /* Override bootstrap style */
    height: initial;
}

/* Vertical Progress */

.widget-vprogress {
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vprogress .progress {
    flex-grow: 1;
    width: var(--jp-widgets-progress-thickness);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

/* Select Widget Styling */

.widget-dropdown {
    height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-dropdown > select {
    padding-right: 20px;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-radius: 0;
    height: inherit;
    flex: 1 1 var(--jp-widgets-inline-width-short);
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    box-sizing: border-box;
    outline: none !important;
    box-shadow: none;
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    vertical-align: top;
    padding-left: calc( var(--jp-widgets-input-padding) * 2);
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: var(--jp-widgets-dropdown-arrow);
}
.widget-dropdown > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-dropdown > select:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */
.widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

/* Select and SelectMultiple */

.widget-select {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    align-items: flex-start;
}

.widget-select > select {
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex: 1 1 var(--jp-widgets-inline-width-short);
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

.widget-select > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.wiget-select > select > option {
    padding-left: var(--jp-widgets-input-padding);
    line-height: var(--jp-widgets-inline-height);
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
    padding-bottom: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
}



/* Toggle Buttons Styling */

.widget-toggle-buttons {
    line-height: var(--jp-widgets-inline-height);
}

.widget-toggle-buttons .widget-toggle-button {
    margin-left: var(--jp-widgets-margin);
    margin-right: var(--jp-widgets-margin);
}

.widget-toggle-buttons .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Radio Buttons Styling */

.widget-radio {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-radio-box {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    box-sizing: border-box;
    flex-grow: 1;
    margin-bottom: var(--jp-widgets-radio-item-height-adjustment);
}

.widget-radio-box label {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    font-size: var(--jp-widgets-font-size);
}

.widget-radio-box input {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    margin: 0 calc( var(--jp-widgets-input-padding) * 2 ) 0 1px;
    float: left;
}

/* Color Picker Styling */

.widget-colorpicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-colorpicker > .widget-colorpicker-input {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: var(--jp-widgets-inline-width-tiny);
}

.widget-colorpicker input[type="color"] {
    width: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-left: none;
    flex-grow: 0;
    flex-shrink: 0;
    box-sizing: border-box;
    align-self: stretch;
    outline: none !important;
}

.widget-colorpicker.concise input[type="color"] {
    border-left: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
}

.widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-colorpicker input[type="text"] {
    flex-grow: 1;
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    box-sizing: border-box;
}

.widget-colorpicker input[type="text"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Date Picker Styling */

.widget-datepicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-datepicker input[type="date"] {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    box-sizing: border-box;
}

.widget-datepicker input[type="date"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-datepicker input[type="date"]:invalid {
    border-color: var(--jp-warn-color1);
}

.widget-datepicker input[type="date"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Play Widget */

.widget-play {
    width: var(--jp-widgets-inline-width-short);
    display: flex;
    align-items: stretch;
}

.widget-play .jupyter-button {
    flex-grow: 1;
    height: auto;
}

.widget-play .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Tab Widget */

.jupyter-widgets.widget-tab {
    display: flex;
    flex-direction: column;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

.jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    padding: var(--jp-widgets-container-padding);
    flex-grow: 1;
    overflow: auto;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    font: var(--jp-widgets-font-size) Helvetica, Arial, sans-serif;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    flex: 0 1 var(--jp-widgets-horizontal-tab-width);
    min-width: 35px;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
    line-height: var(--jp-widgets-horizontal-tab-height);
    margin-left: calc(-1 * var(--jp-border-width));
    padding: 0px 10px;
    background: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    border-bottom: none;
    position: relative;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: var(--jp-ui-font-color0);
    /* We want the background to match the tab content background */
    background: var(--jp-layout-color1);
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + 2 * var(--jp-border-width));
    transform: translateY(var(--jp-border-width));
    overflow: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: calc(-1 * var(--jp-border-width));
    left: calc(-1 * var(--jp-border-width));
    content: '';
    height: var(--jp-widgets-horizontal-tab-top-border);
    width: calc(100% + 2 * var(--jp-border-width));
    background: var(--jp-brand-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\f00d'; /* close */
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: var(--jp-widgets-horizontal-tab-height);
}

/* Accordion Widget */

.p-Collapse {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Collapse-header {
    padding: var(--jp-widgets-input-padding);
    cursor: pointer;
    color: var(--jp-ui-font-color2);
    background-color: var(--jp-layout-color2);
    border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    padding: calc(var(--jp-widgets-container-padding) * 2 / 3) var(--jp-widgets-container-padding);
    font-weight: bold;
}

.p-Collapse-header:hover {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.p-Collapse-open > .p-Collapse-header {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color0);
    cursor: default;
    border-bottom: none;
}

.p-Collapse .p-Collapse-header::before {
    content: '\f0da\00A0';  /* caret-right, non-breaking space */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.p-Collapse-open > .p-Collapse-header::before {
    content: '\f0d7\00A0'; /* caret-down, non-breaking space */
}

.p-Collapse-contents {
    padding: var(--jp-widgets-container-padding);
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    overflow: auto;
}

.p-Accordion {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Accordion .p-Collapse {
    margin-bottom: 0;
}

.p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}



/* HTML widget */

.widget-html, .widget-htmlmath {
    font-size: var(--jp-widgets-font-size);
}

.widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    align-self: stretch;
    flex-grow: 1;
    flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: var(--jp-widgets-inline-height);
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}


/* Image widget  */

.widget-image {
    max-width: 100%;
    height: auto;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8888/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app command_mode" data-jupyter-api-token="2756d7861d8661186c1db2c1e41586f2eb0950d37aa9ede0" data-base-url="/" data-ws-url="" data-notebook-name="Untitled4.ipynb" data-notebook-path="Untitled4.ipynb" dir="ltr"><div id="MathJax_Message" style="display: none;"></div><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=2756d7861d8661186c1db2c1e41586f2eb0950d37aa9ede0" title="dashboard">
      <img src="./Desktop - Jupyter Notebook_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">Desktop</span>
    <span class="checkpoint_status" title="Tue, 21 Sep 2021 18:58">Last Checkpoint: a few seconds ago</span>
    <span class="autosave_status">(autosaved)</span>
</span>


  

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./Desktop - Jupyter Notebook_files/logo-64x64.png" title="Python 3" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="Kernel Idle"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="Command Mode"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" disabled="disabled" style="cursor: help;"><span title="Javascript enabled for notebook display">Trusted</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" id="filelink" data-toggle="dropdown" aria-haspopup="true" aria-controls="file_menu" aria-expanded="false">File</a>
                    <ul id="file_menu" class="dropdown-menu" role="menu" aria-labelledby="filelink">
                        <li id="new_notebook" class="menu_focus_highlight dropdown dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">New Notebook<span class="sr-only">Dropdown</span></a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu" role="menu">
                            <li id="new-notebook-submenu-python3"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Python 3</a></li></ul>
                        </li>
                        <li id="open_notebook" role="none" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="copy_notebook" role="none" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Make a Copy...</a></li>
                        <li id="save_notebook_as" role="none" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Save as...</a></li>
                        <li id="rename_notebook" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Rename...</a></li>
                        <li id="save_checkpoint" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Save and Checkpoint</span><span class="kb"><kbd>⌘S</kbd></span></a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="restore_checkpoint" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Revert to Checkpoint<span class="sr-only">Dropdown</span></a>
                          <ul class="dropdown-menu"><li><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Tuesday, 21 September 2021 18:58</a></li></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="print_preview" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Print Preview</a></li>
                        <li class="dropdown-submenu menu_focus_highlight" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Download as<span class="sr-only">Dropdown</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">AsciiDoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">HTML (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">LaTeX (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">PDF via LaTeX (.pdf)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">reST (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Python (.py)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Reveal.js slides (.slides.html)</a>
                                </li>
                                
                                <li id="download_webpdf">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">PDF via pyppeteer (.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="trust_notebook" role="none" title="Trust the output of this notebook" class="disabled">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Trusted Notebook</a></li>
                        <li class="divider" role="none"></li>
                        <li id="close_and_halt" role="none" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Close and Halt</a></li>
                    </ul>
                </li>

                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" id="editlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="edit_menu">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu" role="menu" aria-labelledby="editlink">
                        <li id="cut_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Cut Cells</span><span class="kb"><kbd>X</kbd></span></a></li>
                        <li id="copy_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Copy Cells</span><span class="kb"><kbd>C</kbd></span></a></li>
                        <li id="paste_cell_above" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Above</span><span class="kb"><kbd>⇧V</kbd></span></a></li>
                        <li id="paste_cell_below" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Below</span><span class="kb"><kbd>V</kbd></span></a></li>
                        <li id="paste_cell_replace" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Delete Cells</span><span class="kb"><kbd>D</kbd>,<kbd>D</kbd></span></a></li>
                        <li id="undelete_cell" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Undo Delete Cells</span><span class="kb"><kbd>Z</kbd></span></a></li>
                        <li class="divider" role="none"></li>
                        <li id="split_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Split Cell</span><span class="kb"><kbd>⌃⇧Minus</kbd></span></a></li>
                        <li id="merge_cell_above" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Merge Cell Above</a></li>
                        <li id="merge_cell_below" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Merge Cell Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="move_cell_up" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Move Cell Up</a></li>
                        <li id="move_cell_down" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Move Cell Down</a></li>
                        <li class="divider" role="none"></li>
                        <li id="edit_nb_metadata" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Edit Notebook Metadata</a></li>
                        <li class="divider" role="none"></li>
                        <li id="find_and_replace" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem"> Find and Replace </a></li>
                        <li class="divider" role="none"></li>
                        <li id="cut_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true">Paste Cell Attachments</a></li>
                        <li class="divider" role="none"></li>
                        <li id="insert_image" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-disabled="true">  Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" id="viewlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="view_menu">View</a>
                    <ul id="view_menu" class="dropdown-menu" role="menu" aria-labelledby="viewlink">
                        <li id="toggle_header" role="none" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" role="none" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" role="none" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Toggle Line Numbers</span><span class="kb"><kbd>⇧L</kbd></span></a>
                        </li>
                        <li id="menu-cell-toolbar" class="menu_focus_highlight dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="None"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">None</a></li><li data-name="Edit%20Metadata"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Edit Metadata</a></li><li data-name="Raw%20Cell%20Format"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Raw Cell Format</a></li><li data-name="Slideshow"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Slideshow</a></li><li data-name="Attachments"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Attachments</a></li><li data-name="Tags"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" id="insertlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="insert_menu">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu" role="menu" aria-labelledby="insertlink">
                        <li id="insert_cell_above" role="none" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Above</span><span class="kb"><kbd>A</kbd></span></a></li>
                        <li id="insert_cell_below" role="none" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Below</span><span class="kb"><kbd>B</kbd></span></a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" id="celllink" data-toggle="dropdown" aria-haspopup="true" aria-controls="cell_menu">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu" role="menu" aria-labelledby="celllink">
                        <li id="run_cell" role="none" title="Run this cell, and move cursor to the next one">
                            <a role="menuitem" href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Run Cells</span><span class="kb"><kbd>⌃↩</kbd></span></a></li>
                        <li id="run_cell_select_below" role="none" title="Run this cell, select below">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Select Below</span><span class="kb"><kbd>⇧↩</kbd></span></a></li>
                        <li id="run_cell_insert_below" role="none" title="Run this cell, insert below">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Insert Below</span><span class="kb"><kbd>⌥↩</kbd></span></a></li>
                        <li id="run_all_cells" role="none" title="Run all cells in the notebook">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Run All</a></li>
                        <li id="run_all_cells_above" role="none" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Run All Above</a></li>
                        <li id="run_all_cells_below" role="none" title="Run this cell and all cells below it">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem">Run All Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="change_cell_type" class="menu_focus_highlight dropdown-submenu" role="none" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Type</a>
                            <ul class="dropdown-menu" role="menu">
                              <li id="to_code" role="none" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Code</span><span class="kb"><kbd>Y</kbd></span></a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Markdown</span><span class="kb"><kbd>M</kbd></span></a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Raw NBConvert</span><span class="kb"><kbd>R</kbd></span></a></li>
                            </ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="current_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Current Outputs</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_current_output" role="none" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Toggle</span><span class="kb"><kbd>O</kbd></span></a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Toggle Scrolling</span><span class="kb"><kbd>⇧O</kbd></span></a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">All Output</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_all_output" role="none" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" data-toggle="dropdown" id="kernellink">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu" aria-labelledby="kernellink">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Interrupt</span><span class="kb"><kbd>I</kbd>,<kbd>I</kbd></span></a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Restart</span><span class="kb"><kbd>0</kbd>,<kbd>0</kbd></span></a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#">Shutdown</a>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="menu-change-kernel" class="menu_focus_highlight dropdown-submenu" role="menuitem">
                            <a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Python 3</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" class="menu-shortcut-container"><span class="action">Keyboard Shortcuts</span><span class="kb"><kbd>H</kbd></span></a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8888/notebooks/Desktop.ipynb#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="Opens in a new window" href="https://docs.python.org/3.8?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://ipython.org/documentation.html?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/numpy/reference/?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/scipy/reference/?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://matplotlib.org/contents.html?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="http://docs.sympy.org/latest/index.html?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://pandas.pydata.org/pandas-docs/stable/?v=20210921123720"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8888/notebooks/Desktop.ipynb#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="Save and Checkpoint" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="insert cell below" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="cut selected cells" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="copy selected cells" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="paste cells below" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="move selected cells up" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="move selected cells down" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" aria-label="Run" title="run cell, select below" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-play fa"></i><span class="toolbar-btn-label">Run</span></button><button class="btn btn-default" title="interrupt the kernel" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="restart the kernel (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="restart the kernel, then re-run the whole notebook (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" aria-label="combobox, select cell type" role="combobox" class="form-control select-xs"><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw NBConvert</option><option value="heading">Heading</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group" id="cmd_palette"><button class="btn btn-default" title="open the command palette" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 404px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[1]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 124.594px; left: 239.281px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="width: 18px; pointer-events: none;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true" style="height: 18px; pointer-events: none;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 326.312px; margin-bottom: 0px; border-right-width: 50px; min-height: 147px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 239.281px; top: 119px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">p</span><span class="cm-operator">=</span><span class="cm-builtin">float</span>(<span class="cm-builtin">input</span>(<span class="cm-string">"enter the principle:"</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">r</span><span class="cm-operator">=</span><span class="cm-builtin">float</span>(<span class="cm-builtin">input</span>(<span class="cm-string">"enter the rate:"</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">t</span><span class="cm-operator">=</span><span class="cm-builtin">float</span>(<span class="cm-builtin">input</span>(<span class="cm-string">"enter the time:"</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"principle:"</span>,<span class="cm-variable">p</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"rate:"</span>,<span class="cm-variable">r</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"time:"</span>,<span class="cm-variable">t</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">si</span><span class="cm-operator">=</span>(<span class="cm-variable">p</span><span class="cm-operator">*</span><span class="cm-variable">r</span><span class="cm-operator">*</span><span class="cm-variable">t</span>)<span class="cm-operator">/</span><span class="cm-number">100</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"simple interest:"</span>,<span class="cm-variable">si</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 50px; width: 1px; border-bottom: 0px solid transparent; top: 147px;"></div><div class="CodeMirror-gutters" style="display: none; height: 197px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>enter the principle:1
enter the rate:2
enter the time:2
principle: 1.0
rate: 2.0
time: 2.0
simple interest: 0.04
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered selected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="width: 18px; pointer-events: none;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true" style="height: 18px; pointer-events: none;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 7px; margin-bottom: 0px; border-right-width: 50px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 50px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 78px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="display:none"><div class="tooltipbuttons"><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">Close</span></a><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="button" class="ui-button" id="expanbutton" title="Grow the tooltip vertically (press shift-tab twice)"><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="button" class="ui-button" title="show the current docstring in pager (press shift-tab 4 times)"><span class="ui-icon ui-icon-arrowstop-l-n">Open in Pager</span></a><a href="http://localhost:8888/notebooks/Desktop.ipynb#" role="button" class="ui-button" title="Tooltip will linger for 10 seconds while you type" style="display: none;"><span class="ui-icon ui-icon-clock">Close</span></a></div><div class="pretooltiparrow"></div><div class="tooltiptext smalltooltip"></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="Open the pager in an external window" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="Close the pager" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "6.3.0", "notebook_path": "/opt/anaconda3/lib/python3.8/site-packages/notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.8.8 (default, Apr 13 2021, 12:59:45) \n[Clang 10.0.0 ]", "sys_executable": "/opt/anaconda3/bin/python", "sys_platform": "darwin", "platform": "macOS-10.13.6-x86_64-i386-64bit", "os_name": "posix", "default_encoding": "utf-8"};
</script>

<script src="./Desktop - Jupyter Notebook_files/encoding.js" charset="utf-8"></script>

<script src="./Desktop - Jupyter Notebook_files/main.min.js" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
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


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div></body></html>