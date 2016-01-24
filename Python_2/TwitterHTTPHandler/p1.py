from http.server import HTTPServer, BaseHTTPRequestHandler
import csv

class TwitterHTTPRequestHandler(BaseHTTPRequestHandler):
    def _write_back(self, string):
        self.wfile.write(bytes(string, 'UTF-8'))

    def _write_back_line(self, string):
        self._write_back(string + '\n')

    def _read_csv(self):
        lines = list()
        with open("tweets.csv") as f:
            for row in csv.reader(f):
                lines.append(row)
        return lines

    def do_GET(self):
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        
        parts = self.path.split('/')[1:]


        if len(parts) == 1:
            lines = self._read_csv()
            for line in lines:
                self._write_back_line("@%s: %s" % (line[0], line[1]))
        
        elif len(parts) == 2 and parts[0].endswith('view'):
            username = parts[1]
            lines = self._read_csv()
            for line in lines:
                if username in line:
                    self._write_back_line("@%s: %s" % (line[0], line[1]))

        elif len(parts) == 2 and parts[0].endswith('mentions'):
            mention = parts[1]
            lines = self._read_csv()
            for line in lines:
                if line[1].find("@" + parts[1] + " ") >= 0:
                    self._write_back_line("@%s: %s" % (line[0], line[1]))
                

        else:
            self._write_back_line('Could not interpret your request!')
            self._write_back_line('Request: ' + self.path)

def main():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, TwitterHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
