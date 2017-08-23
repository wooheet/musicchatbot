#!/usr/bin/env python3

import cgi
from botengine import make_reply

# 입력 양식의 글자 추출하기 --- (※1)
form = cgi.FieldStorage()

# 메인 처리 --- (※2)
def main():
    m = form.getvalue("m", default="")
    if   m == "" : show_form()
    elif m == "say" : api_say()

# 사용자의 입력에 응답하기 --- (※3)
def api_say():
    print("Content-Type: text/plain; charset=euc-kr")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)

# 입력 양식 출력하기 --- (※4)
def show_form():
    print("Content-Type: text/html; charset=euc-kr")
    print("")
    print("""
    <html>
        <meta charset="euc-kr">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Chatbot</title>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">
                <style type="text/css">
                        .bot { text-align: left; }
                        .usr { text-align: right; }
                        
                    .fixed-panel {
                        min-height: 400px;
                        max-height: 400px;
                        background-color: #19313c;
                        color: white;
                        overflow: auto;
                    }
                    .media-list {
                        overflow: auto;
                        clear: both;
                        display: table;
                        overflow-wrap: break-word;
                        word-wrap: break-word;
                        word-break: normal;
                        line-break: strict;        
                   }
                    .panel {
                        margin-bottom: 20px;
                        background-color: #fff;
                        border: 6px solid transparent;
                        border-radius: 25px;
                        -webkit-box-shadow: 0 1px 1px rgba(0,0,0,.05);
                        box-shadow: 0 1px 1px rgba(0,0,0,.05);
                    }
                    .panel-info {
                         border-color: #0c2735;
                    }
                    .panel-info>.panel-heading {
                        color: #fff;
                        background-color: #0c2735;
                        border-color: #0c2735;
                    }
                    .panel-footer {
                        padding: 10px 15px;
                        background-color: #0c2735;
                        border-top: 1px solid #0c2735;
                        border-bottom-right-radius: 3px;
                        border-bottom-left-radius: 3px;
                        color: #fff;
                    }
                    body {
                        /* Permalink - use to edit and share this gradient: http://colorzilla.com/gradient-editor/#608f95+0,008588+9,0c2449+52,1a1e3b+100 */
                        background: rgb(96,143,149); /* Old browsers */
                        background: -moz-linear-gradient(-45deg, rgba(96,143,149,1) 0%, rgba(0,133,136,1) 9%, rgba(12,36,73,1) 52%, rgba(26,30,59,1) 100%); /* FF3.6-15 */
                        background: -webkit-linear-gradient(-45deg, rgba(96,143,149,1) 0%,rgba(0,133,136,1) 9%,rgba(12,36,73,1) 52%,rgba(26,30,59,1) 100%); /* Chrome10-25,Safari5.1-6 */
                        background: linear-gradient(135deg, rgba(96,143,149,1) 0%,rgba(0,133,136,1) 100%,rgba(12,36,73,1) 52%,rgba(26,30,59,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
                        filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#608f95', endColorstr='#1a1e3b',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
                    }
                </style>
                
                <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
        
        </head>
        
        <body>
            <div class="container background-color: rgb(255,0,255);">
                    <div class="row"><br/>
                        <div class="col-md-4 col-md-offset-4">
                            <div id="chatPanel" class="panel panel-info">
                                <div class="panel-heading">
                                    <strong><span class="fa fa-wechat"></span> Musicher</strong>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
                                    <button class="btn btn-link" type="button" id="save">Save <span class="glyphicon glyphicon-save"></span></button>
                                    <button class="btn btn-link" type="button" id="quit">Quit <span class="glyphicon glyphicon-arrow-left"></span></button>
                                </div>
                                <div class="panel-body fixed-panel">
                                    <ul class="media-list" id="chat">
                                    </ul>
                                </div>
                                <div class="panel-footer">                                    
                                    <br/>
                                        <div class="input-group">
                                            <input type="text" class="form-control" placeholder="Enter Message" name="txt" id="txt" autofocus/>
                                            <span class="input-group-btn">
                                                <button class="btn btn-link" type="button" id="chatbot-form-btn" onclick="say()">SEND <span class="glyphicon glyphicon-send"></span></button>
                                            </span>
                                        </div>
                                   <br/>
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>                
            <script>
            
                var url = "./musicchatbot.py";
                
                 function say() {
                      var txt = $('#txt').val();
                      $.get(url, {"m":"say","txt":txt},
                        function(res) {
                          var html = "<div class='usr'><span>" + esc(txt) +
                            "</span>: 나</div><div class='bot'> 봇:<span>" + 
                            esc(res) + "</span></div>";
                          $('#chat').html($('#chat').html()+html);
                          $('#txt').val('').focus();
                        });
                    }
                    function esc(s) {
                        return s.replace('&', '&amp;').replace('<','&lt;')
                                .replace('>', '&gt;');
                    }
                    
            </script>
        </body>
    </html>
    """)

main()
