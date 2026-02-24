const net = require("net");

const server = net.createServer(socket => {
    socket.on("data", data => {
        console.log("--- Browser Request ---");
        console.log(data.toString()); // You'll see the HTTP headers here

        // We format a basic HTTP response
        const response = 
            "HTTP/1.1 403 TUl\r\n" +          // Status Line
            "Content-Type: text/html\r\n" +  // Header: Telling the browser it's HTML
            "Content-Length: 20\r\n" +       // Header: Size of the body
            "\r\n" +                         // The required blank line
            "<h1>asdfasdfasdf</h1>";          // The Body

        socket.write(response);
        socket.end(); // Close the connection so the browser stops "spinning"
    });
});

server.listen(8080, () => {
    console.log("Server listening on http://localhost:8080");
});