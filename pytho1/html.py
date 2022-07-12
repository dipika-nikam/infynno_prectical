import re
string ="""<!doctype html>
            <html dir="ltr" lang="en">
              <head>
                <meta charset="utf-8">
                <title>New Tab</title>
                <style>
                  body {
                    background: #353535;
                    margin: 0;
                  }
            
                  #backgroundImage {
                    border: none;
                    height: 100%;
                    pointer-events: none;
                    position: fixed;
                    top: 0;
                    visibility: hidden;
                    width: 100%;
                  }
            
                  [show-background-image] #backgroundImage {
                    visibility: visible;
                  }
                </style>
              </head>
              <body>
                <iframe id="backgroundImage" src="chrome-untrusted://new-tab-page/custom_background_image?url=https%3A%2F%2Flh6.googleusercontent.com%2Fproxy%2FfUx750lchxFJb3f37v_-4iJPzcTKtJbd5LDRO7S9Xy7nkPzh7HFU61tN36j4Diaa9Yk3K7kWshRwmqcrulnhbeJrRpIn79PjHN-N%3Dw3840-h2160-p-k-no-nd-mv"></iframe>
                <ntp-app></ntp-app>
                <script type="module" src="new_tab_page.js"></script>
                <link rel="stylesheet" href="chrome://resources/css/text_defaults_md.css">
                <link rel="stylesheet" href="shared_vars.css">
              </body>
            </html>"""
# check = re.compile('<[^>]+>').sub('', string)
# print(check)
print(re.compile('<[a-z]{6} .*></[a-z]{6}>').sub('',string))

