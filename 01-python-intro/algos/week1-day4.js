const str1 = "aaaabbcddd";
const expected1 = "a4bbcd3";
const expected1b = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

const str5 = "abbbbbbbbbbbbbbbbb"
const expected5 = "ab17"

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */




function encodeStr(str) {
    newStr = ""
    for( i = 0; i < str.length; i++) {
        count = 1;
        while(str[i] === str[i+1]){
            count++;
            i++
            
        }
        newStr += str[i] + count
    }
    console.log(newStr)
}

encodeStr(str1)
encodeStr(str2)
encodeStr(str3)
encodeStr(str4)
encodeStr(str5)
