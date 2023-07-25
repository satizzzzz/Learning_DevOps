# Misc Questions

## 𝗪𝗵𝗮𝘁 𝗵𝗮𝗽𝗽𝗲𝗻𝘀 𝘄𝗵𝗲𝗻 𝘆𝗼𝘂 𝘁𝘆𝗽𝗲 𝗮 𝗨𝗥𝗟 𝗶𝗻𝘁𝗼 𝘆𝗼𝘂𝗿 𝗯𝗿𝗼𝘄𝘀𝗲𝗿?

```
1. You type the URL, which has 4️⃣ parts:

- 🛡️ Protocol (e.g., https://)
- 🏠 Domain (e.g., example.com)
- 📁 Directory (e.g., /blog)
- 📄 Resource (e.g., /post)

2. Your browser hunts for the server's IP address 🔎:

🔹 It checks various caches (browser, OS, local network, ISP)
🔹 If not found, it does a DNS lookup 🔍

3. Connection time! ⏱️ The browser creates a TCP connection with the server.

4. The browser sends an HTTP request 📨 to the server:

GET /blog/post HTTP/1.1
Host: example.com

The server processes the request and sends back an HTTP response, including the status code (200 for success) and the HTML content:

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
 <head>
 <title>Example Post</title>
 </head>
 <body>
 <h1>Welcome to the Example Post!</h1>
 </body>
</html>

5. Finally, the browser renders the HTML content, and voila! The webpage appears! 🎉
```
![URL_access](https://github.com/satizzzzz/Learning_DevOps/assets/26127571/4469b2ce-1271-46d9-9355-569455b75b7f)


