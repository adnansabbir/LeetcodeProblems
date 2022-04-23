baseUrl = "http://tinyurl.com/"
length = 1
map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
encodedURL = {}
decodedURL = {}


const _generateRandomHash = () => {
    let newHash = ""
    for (let i = 0; i < hashSize; i++){
        const randomIdx = Math.floor(Math.random() * map.length)
        newHash += map[randomIdx]
    }

    return encodedURL[newHash] === undefined ? newHash : _generateRandomHash()
}
// /**
//  * Encodes a URL to a shortened URL.
//  *
//  * @param {string} longUrl
//  * @return {string}
//  */
var encode = function(longUrl) {
    if(encodedURL[longUrl] !== undefined){
      return baseUrl+encodedURL[longUrl]
    }  
    
    const newHash = length++
    encodedURL[longUrl] = newHash
    decodedURL[newHash] = longUrl
    
    return baseUrl + newHash
};

// /**
//  * Decodes a shortened URL to its original URL.
//  *
//  * @param {string} shortUrl
//  * @return {string}
//  */
var decode = function(shortUrl) {
    const hashKey = shortUrl.substring(baseUrl.length)
    return decodedURL[hashKey] || null
};

// /**
//  * Your functions will be called as such:
//  * decode(encode(url));
//  */