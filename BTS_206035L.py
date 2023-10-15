<!DOCTYPE html>
<!-- saved from url=(0026)http://localhost:8888/tree -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Home Page - Select or create a notebook</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon.ico?v=50afa725b5de8b00030139d09b38620224d4e7dba47c07ef0e86d4643f30c9bfe6bb7e1a4a1c561aa32834480909a4b6fe7cd1e17f7159330b6b5914bf45a880">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./BTS_206035L_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./BTS_206035L_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="./BTS_206035L_files/style.min.css" type="text/css">
    
    <link rel="stylesheet" href="./BTS_206035L_files/custom.css" type="text/css">
    <script src="./BTS_206035L_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./BTS_206035L_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./BTS_206035L_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./BTS_206035L_files/index.js.download" type="text/javascript"></script>
    <script src="./BTS_206035L_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20230510112852",
          
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

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./BTS_206035L_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./BTS_206035L_files/custom.js.download"></script></head>

<body class="" data-jupyter-api-token="a5b4503a0c57dfab12f4ed4cc884ff5cb14c14adbaad1e39" data-base-url="/" data-notebook-path="" data-terminals-available="True" data-server-root="C:\Users\Nathalie" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=a5b4503a0c57dfab12f4ed4cc884ff5cb14c14adbaad1e39" title="dashboard">
      <img src="./BTS_206035L_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  
  <span class="flex-spacer"></span>
  
  
  
    <span id="shutdown_widget">
      <button id="shutdown" class="btn btn-sm navbar-btn" title="Stop the Jupyter server">
          Quit
      </button>
    </span>
  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site" style="display: block; height: 689px;">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable" role="main">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="http://localhost:8888/tree#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="http://localhost:8888/tree#running" data-toggle="tab">Running</a></li>
        <li><a href="http://localhost:8888/tree#clusters" data-toggle="tab" class="clusters_tab_link">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions" style="display: none;">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" aria-label="Duplicate selected" class="duplicate-button btn btn-default btn-xs" aria-describedby="tooltip1" style="display: inline-block;">Duplicate </button>
                  <div role="tooltip" id="tooltip1">Duplicate selected</div>
                  <button title="Rename selected" aria-label="Rename selected" class="rename-button btn btn-default btn-xs" aria-describedby="tooltip2" style="display: inline-block;">Rename</button>
                  <div role="tooltip" id="tooltip2">Rename selected</div> 
                  <button title="Move selected" aria-label="Move selected" class="move-button btn btn-default btn-xs" aria-describedby="tooltip3" style="display: inline-block;">Move</button>
                  <div role="tooltip" id="tooltip3">Move selected</div> 
                  <button title="Download selected" aria-label="Download selected" class="download-button btn btn-default btn-xs" aria-describedby="tooltip4" style="display: inline-block;">Download</button>
                  <div role="tooltip" id="tooltip4">Download selected</div>
                  <button title="Shutdown selected notebook(s)" aria-label="Shutdown selected notebook(s)" class="shutdown-button btn btn-default btn-xs btn-warning" aria-describedby="tooltip5" style="display: none;">Shutdown</button>
                  <div role="tooltip" id="tooltip5">Shutdown selected notebook(s)</div>  
                  <button title="View selected" aria-label="View selected" class="view-button btn btn-default btn-xs" aria-describedby="tooltip6" style="display: inline-block;">View</button>
                  <div role="tooltip" id="tooltip6">View selected</div> 
                  <button title="Edit selected" aria-label="Edit selected" class="edit-button btn btn-default btn-xs" aria-describedby="tooltip7" style="display: inline-block;">Edit</button>
                  <div role="tooltip" id="tooltip7">Edit selected</div>  
                  <button title="Delete selected" aria-label="Delete selected" class="delete-button btn btn-default btn-xs btn-danger" aria-describedby="tooltip8" style="display: inline-block;">
                    <i class="fa fa-trash"></i>
                  </button>
                  <div role="tooltip" id="tooltip8">Delete selected</div>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id="alternate_upload" class="alternate_upload">
                  <span id="notebook_list_info" class="toolbar_info">
                  <span id="upload_span" class="btn btn-xs btn-default btn-upload" role="button" tabindex="0">
                    <input id="upload_span_input" title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple="multiple" tabindex="-1">
                    Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" id="new-dropdown-button" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu" role="menu">
                    <li role="menuitem" class="dropdown-header" id="notebook-kernels">Notebook:</li><li id="kernel-python3"><a aria-label="python3" role="menuitem" href="http://localhost:8888/tree#" title="Create a new notebook with Python 3 (ipykernel)">Python 3 (ipykernel)</a></li>
                    <li role="presentation" class="divider"></li>
                    <li role="menuitem" class="dropdown-header">Other:</li>
                    <li role="none" id="new-file">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Text File</a>
                    </li>
                    <li role="none" id="new-folder">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Folder</a>
                    </li>
                    
                    <li role="none" id="new-terminal">
                        <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Terminal</a>
                    </li>
                    
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" aria-label="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list" class="list_container">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" aria-label="Selected, 1 items" type="button" class="btn btn-default btn-xs" id="button-select-all" role="checkbox">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all" tabindex="-1"><span id="counter-select-all">1</span>
                </button>
                <button title="Select Folders/All Notebooks/Running/Files" class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="sr-only">checkbox</span>
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id="selector-menu" class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="none"><a id="select-folders" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i>&nbsp;Folders</a></li>
                  <li role="none"><a id="select-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i>&nbsp;All Notebooks</a></li>
                  <li role="none"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i>&nbsp;Running</a></li>
                  <li role="none"><a id="select-files" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i>&nbsp;Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb"><li><a href="http://localhost:8888/tree" title="Link to root folder"><i class="fa fa-folder"></i></a></li><li><a href="http://localhost:8888/tree"></a></li></ul>
              </div>
              <div id="sort_buttons" class="pull-right">
                <div id="sort_name" class="sort_button">
                  <button type="button" class="btn btn-xs btn-default sort-action" id="sort-name" aria-label="Sort by name">
                        Name
                        <i class="fa fa-arrow-down"></i>
                  </button>
                </div>
                <div id="last_modified" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="last-modified" aria-label="Sort by last modified">
                        Last Modified
                        <i class="fa"></i>
                    </button>
                </div>
                <div id="file_size" class="sort_button">
                    <button type="button" class="btn btn-xs btn-default sort-action" id="file-size" aria-label="Sort by file size">
                        File size
                        <i class="fa"></i>
                    </button>
                </div>
              </div>
            </div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/3D%20Objects"><span class="item_name">3D Objects</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/anaconda3"><span class="item_name">anaconda3</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-12-12 16:19">5 months ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Contacts"><span class="item_name">Contacts</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Desktop"><span class="item_name">Desktop</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-12 14:15">a month ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Documents"><span class="item_name">Documents</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-30 08:52">10 days ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Downloads"><span class="item_name">Downloads</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-05-10 11:52">4 hours ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Favorites"><span class="item_name">Favorites</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Links"><span class="item_name">Links</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Microsoft"><span class="item_name">Microsoft</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-06 10:51">7 months ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Music"><span class="item_name">Music</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/OneDrive"><span class="item_name">OneDrive</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-25 14:41">7 months ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/OneDrive%20-%20University%20of%20Moratuwa"><span class="item_name">OneDrive - University of Moratuwa</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-05-10 09:49">6 hours ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Pictures"><span class="item_name">Pictures</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-28 07:35">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Saved%20Games"><span class="item_name">Saved Games</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:34">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Searches"><span class="item_name">Searches</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-02 11:35">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Videos"><span class="item_name">Videos</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-04 09:18">a year ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20%20%20%20Variables%20day2.ipynb" target="_blank"><span class="item_name">    Variables day2.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-17 22:45">8 months ago</span><span class="file_size pull-right">1.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20%20%20dictionaries%20day4.ipynb" target="_blank"><span class="item_name">   dictionaries day4.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-28 12:06">7 months ago</span><span class="file_size pull-right">25.2 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20%20Forloops%20%20day%205.ipynb" target="_blank"><span class="item_name">  Forloops  day 5.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-30 21:19">7 months ago</span><span class="file_size pull-right">18.1 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20BST_206035L.py.ipynb" target="_blank"><span class="item_name"> BST_206035L.py.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-05-10 15:58">10 minutes ago</span><span class="file_size pull-right">5.52 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Cryptography%20day11.12.ipynb" target="_blank"><span class="item_name"> Cryptography day11.12.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-18 17:51">7 months ago</span><span class="file_size pull-right">10.3 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20D.S%20.A%20%20stack.ipynb" target="_blank"><span class="item_name"> D.S .A  stack.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-10 14:52">a month ago</span><span class="file_size pull-right">5.85 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20D.S.A%20Arrays.ipynb" target="_blank"><span class="item_name"> D.S.A Arrays.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-09 13:58">a month ago</span><span class="file_size pull-right">6.26 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20D.S.A%20linked%20list.ipynb" target="_blank"><span class="item_name"> D.S.A linked list.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-10 12:55">a month ago</span><span class="file_size pull-right">15.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20D.S.A%20Que.ipynb" target="_blank"><span class="item_name"> D.S.A Que.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-10 17:35">a month ago</span><span class="file_size pull-right">6.51 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Day%207%20practice%20excercise.ipynb" target="_blank"><span class="item_name"> Day 7 practice excercise.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-10 15:08">7 months ago</span><span class="file_size pull-right">12.6 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20day%208%20Strings.ipynb" target="_blank"><span class="item_name"> day 8 Strings.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-13 09:07">7 months ago</span><span class="file_size pull-right">22.6 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Excersice%20no%202%20day%2012.ipynb" target="_blank"><span class="item_name"> Excersice no 2 day 12.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-28 11:04">6 months ago</span><span class="file_size pull-right">16.9 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20exercise%2001%20day%207.ipynb" target="_blank"><span class="item_name"> exercise 01 day 7.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-03 23:09">7 months ago</span><span class="file_size pull-right">832 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Exersice%201%20day%2007.ipynb" target="_blank"><span class="item_name"> Exersice 1 day 07.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-04-13 17:53">a year ago</span><span class="file_size pull-right">17.6 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Factorial%20day%2011.ipynb" target="_blank"><span class="item_name"> Factorial day 11.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-17 00:18">7 months ago</span><span class="file_size pull-right">34.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20For%20loop%20day5.ipynb" target="_blank"><span class="item_name"> For loop day5.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-14 18:49">a year ago</span><span class="file_size pull-right">36.3 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20if%20conditions%20and%20branching%20day%204.ipynb" target="_blank"><span class="item_name"> if conditions and branching day 4.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-30 14:13">7 months ago</span><span class="file_size pull-right">9.4 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20lists%20day3%20.ipynb" target="_blank"><span class="item_name"> lists day3 .ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-26 17:00">7 months ago</span><span class="file_size pull-right">59.8 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Matrices%20using%20Python%20lab%201%20sem%203.ipynb" target="_blank"><span class="item_name"> Matrices using Python lab 1 sem 3.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-07-25 14:58">9 months ago</span><span class="file_size pull-right">7.31 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Python%20assignment.ipynb" target="_blank"><span class="item_name"> Python assignment.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-02-16 09:46">a year ago</span><span class="file_size pull-right">3.5 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20python%20day%201.ipynb" target="_blank"><span class="item_name"> python day 1.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-03 14:26">8 months ago</span><span class="file_size pull-right">588 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Python%20functions(methods).ipynb" target="_blank"><span class="item_name"> Python functions(methods).ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-13 16:59">7 months ago</span><span class="file_size pull-right">8.99 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20python%20modules%20and%20libraries%20day%2013.ipynb" target="_blank"><span class="item_name"> python modules and libraries day 13.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-26 18:58">6 months ago</span><span class="file_size pull-right">10.7 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20sets%20day%2003.ipynb" target="_blank"><span class="item_name"> sets day 03.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-26 18:33">7 months ago</span><span class="file_size pull-right">8.71 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20The%20jacobi%20%20method.ipynb" target="_blank"><span class="item_name"> The jacobi  method.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-07-26 10:47">9 months ago</span><span class="file_size pull-right">21.6 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20Tuples%20day%2003.ipynb" target="_blank"><span class="item_name"> Tuples day 03.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-26 17:17">7 months ago</span><span class="file_size pull-right">4.88 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20while%20loop%20part2%20day%206.ipynb" target="_blank"><span class="item_name"> while loop part2 day 6.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-19 11:46">a year ago</span><span class="file_size pull-right">17.4 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20while%20loop.%20day6.ipynb" target="_blank"><span class="item_name"> while loop. day6.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-14 22:43">a year ago</span><span class="file_size pull-right">90.6 MB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/%20while%20loops%20day6.ipynb" target="_blank"><span class="item_name"> while loops day6.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-02 16:39">7 months ago</span><span class="file_size pull-right">8.59 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Day%207%20Practice%20excercise.ipynb" target="_blank"><span class="item_name">Day 7 Practice excercise.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-14 16:27">7 months ago</span><span class="file_size pull-right">28.2 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/day%208%20strings.ipynb" target="_blank"><span class="item_name">day 8 strings.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-10 23:47">7 months ago</span><span class="file_size pull-right">15.1 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/forloop%20day%205.6.ipynb" target="_blank"><span class="item_name">forloop day 5.6.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-02 13:03">7 months ago</span><span class="file_size pull-right">25.8 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/if%20conditionals%20and%20branching%20day4%205.ipynb" target="_blank"><span class="item_name">if conditionals and branching day4 5.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-10 10:46">a year ago</span><span class="file_size pull-right">13.1 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/methods%20day%2009.ipynb" target="_blank"><span class="item_name">methods day 09.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-10-14 09:08">7 months ago</span><span class="file_size pull-right">17.1 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled.ipynb" target="_blank"><span class="item_name">Untitled.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-01-26 15:25">3 months ago</span><span class="file_size pull-right">2.65 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled1.ipynb" target="_blank"><span class="item_name">Untitled1.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-03-29 10:10">a month ago</span><span class="file_size pull-right">1.65 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled2.ipynb" target="_blank"><span class="item_name">Untitled2.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-03-29 11:03">a month ago</span><span class="file_size pull-right">1.66 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled3.ipynb" target="_blank"><span class="item_name">Untitled3.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-26 09:50">14 days ago</span><span class="file_size pull-right">1.95 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/variables%20day%202.ipynb" target="_blank"><span class="item_name">variables day 2.ipynb</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-09-17 22:57">8 months ago</span><span class="file_size pull-right">3.28 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/206035l-Copy1.LL.PY" target="_blank"><span class="item_name">206035l-Copy1.LL.PY</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-03-29 10:11">a month ago</span><span class="file_size pull-right">1.65 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/206035l.LL.PY" target="_blank"><span class="item_name">206035l.LL.PY</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-03-29 11:02">a month ago</span><span class="file_size pull-right">4.59 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/206035l_mp.py" target="_blank"><span class="item_name">206035l_mp.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-03-29 11:05">a month ago</span><span class="file_size pull-right">1.66 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/BST_206035L.py" target="_blank"><span class="item_name">BST_206035L.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-05-10 16:04">5 minutes ago</span><span class="file_size pull-right">5.45 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/file.txt" target="_blank"><span class="item_name">file.txt</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-03-02 08:21">a year ago</span><span class="file_size pull-right">0 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/Iterative%20Methods.ipynb.txt" target="_blank"><span class="item_name">Iterative Methods.ipynb.txt</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-07-17 22:10">10 months ago</span><span class="file_size pull-right">13.2 kB</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/Tree" target="_blank"><span class="item_name">Tree</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2023-04-10 17:41">a month ago</span><span class="file_size pull-right">0 B</span></div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/untitled" target="_blank"><span class="item_name">untitled</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="running-indicator" style="visibility: hidden;">Running</div></div><div class="pull-right"><span class="item_modified pull-left" title="2022-07-20 17:23">10 months ago</span><span class="file_size pull-right">0 B</span></div></div></div></div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info" class="toolbar_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right toolbar_buttons">
              <button id="refresh_running_list" title="Refresh running list" aria-label="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="http://localhost:8888/tree#">
                  Terminals
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list" class="list_container">
                    <div id="terminal_list_header" class="row list_placeholder">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="http://localhost:8888/tree#">
                  Notebooks
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list" class="list_container">
                    <div id="running_list_placeholder" class="row list_placeholder" style="display: none;">
                      <div> There are no notebooks running. </div>
                    </div>
                  <div class="list_item row"><div class="col-md-12"><i class="item_icon running_notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/BST_206035L.py" target="_blank"><span class="item_name">BST_206035L.py</span></a><div class="pull-right"><div class="item_buttons pull-left"><div class="kernel-name">Python 3 (ipykernel)</div><button class="btn btn-warning btn-xs">Shutdown</button></div><div class="pull-right"><span class="item_modified pull-left" title="2023-05-10 16:09">seconds ago</span><span class="file_size pull-right">&nbsp;</span></div></div></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="clusters" class="tab-pane">
          Clusters tab is now provided by IPython parallel.
          See '<a href="https://github.com/ipython/ipyparallel">IPython parallel</a>' for installation details.
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content -->
  </div><!-- ipython-main-app  -->


</div>





    

    <script src="./BTS_206035L_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>

    <script type="text/javascript">
      $('#element').tooltip('enable')
    </script>


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

      #changes done in .py
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>