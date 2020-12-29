#!/bin/bash

filename="/home/kali/Documents/PruebasTT/InitialAccess/test.pdf"
subject="Subject of my email"
txtmessage="This is the message I want to send"

{
sleep 1;
echo "EHLO lab.local"
sleep 1;
echo "MAIL FROM:saguaro@lab.local"
sleep 1;
echo "RCPT TO:Administrator@lab.local"
sleep 1;
echo "DATA"
sleep 1;
echo "Subject:" $subject
sleep 1;
echo "Content-Type: multipart/mixed; boundary="KkK170891tpbkKk__FV_KKKkkkjjwq""
sleep 1;
echo ""
sleep 1;
echo "This is a MIME formatted message.  If you see this text it means that your"
sleep 1;
echo "email software does not support MIME formatted messages."
sleep 1;
echo ""
sleep 1;
echo "--KkK170891tpbkKk__FV_KKKkkkjjwq"
sleep 1;
echo "Content-Type: text/plain; charset=UTF-8; format=flowed"
sleep 1;
echo "Content-Disposition: inline"
sleep 1;
echo ""
sleep 1;
echo $txtmessage
sleep 1;
echo ""
sleep 1;
echo ""
sleep 1;
echo "--KkK170891tpbkKk__FV_KKKkkkjjwq"
sleep 1;
echo "Content-Type: file --mime-type -b filename-$(date +%y%m%d).zip; name=filename-$(date +%y%m%d).zip"
sleep 1;
echo "Content-Transfer-Encoding: base64"
sleep 1;
echo "Content-Disposition: attachment; filename="filename-$(date +%y%m%d).zip";"
sleep 1;
echo ""
sleep 1;
# The content is encoded in base64.
cat $filename | base64;
sleep 1;
echo ""
sleep 1;
echo ""
sleep 1;
echo "--KkK170891tpbkKk__FV_KKKkkkjjwq--"
sleep 1;
echo ""
sleep 1;
echo "."
sleep 1;
echo "quit"
} | telnet 10.10.1.10 25
