import random

class Codec:
    def __init__(self):
        self.long_2_tiny = {}
        self.tiny_2_long = {}
        self.url = "https://tinyurl.com/"
        self.alpha_num = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    
    def _newCode(self):
        res = ''
        while res == '':
            code = [random.choice(self.alpha_num) for _ in range(7)]
            res = ''.join(code) 
            if res in self.tiny_2_long:
                res = ''
        return res

    def encode(self, long_url:str) ->str:
        if long_url in self.long_2_tiny:
            return self.url + self.long_2_tiny[long_url]
        code = self._newCode()
        self.tiny_2_long[code] = long_url
        self.long_2_tiny[long_url] = code
        return self.url+code
    
    def decode(self, url:str)->str:
        tiny_url = url.split("/")[-1]
        return self.tiny_2_long.get(tiny_url,"")


if __name__ == "__main__":
    def test_basic_encode_decode():
        codec = Codec()
        long_url = "https://www.example.com/very/long/url/path"
        encoded = codec.encode(long_url)
        assert encoded.startswith("https://tinyurl.com/")
        assert len(encoded.split("/")[-1]) == 7
        decoded = codec.decode(encoded)
        assert decoded == long_url
        print("✓ test_basic_encode_decode passed")

    def test_encode_same_url_twice():
        codec = Codec()
        long_url = "https://www.example.com/test"
        encoded1 = codec.encode(long_url)
        encoded2 = codec.encode(long_url)
        assert encoded1 == encoded2
        print("✓ test_encode_same_url_twice passed")

    def test_different_urls_different_codes():
        codec = Codec()
        url1 = "https://www.example.com/page1"
        url2 = "https://www.example.com/page2"
        encoded1 = codec.encode(url1)
        encoded2 = codec.encode(url2)
        assert encoded1 != encoded2
        print("✓ test_different_urls_different_codes passed")

    def test_decode_nonexistent_url():
        codec = Codec()
        result = codec.decode("https://tinyurl.com/nonexist")
        assert result == ""
        print("✓ test_decode_nonexistent_url passed")

    def test_multiple_encode_decode():
        codec = Codec()
        urls = [
            "https://leetcode.com/problems/encode-and-decode-tinyurl/",
            "https://www.google.com",
            "https://github.com/user/repo",
            "https://stackoverflow.com/questions/12345/some-question"
        ]
        encoded_urls = []
        for url in urls:
            encoded = codec.encode(url)
            encoded_urls.append(encoded)
            assert encoded.startswith("https://tinyurl.com/")
        
        for i, encoded in enumerate(encoded_urls):
            decoded = codec.decode(encoded)
            assert decoded == urls[i]
        print("✓ test_multiple_encode_decode passed")

    test_basic_encode_decode()
    test_encode_same_url_twice()
    test_different_urls_different_codes()
    test_decode_nonexistent_url()
    test_multiple_encode_decode()
    print("\nAll tests passed! ✓")