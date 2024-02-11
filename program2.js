let input = process.argv.slice(2);
let words = [''];
let repeats = [];

//no input = error
if (process.argv.length === 2){
    console.error("ERROR: You must provide at least one string");
}
else{
    for(let i = 0;  i<input.length; i++){
        part = input[i].split(" ");

        for(let n = 0; n<part.length;n++){
            withoutq = part[n].replace(/"/g, "");
            findRepeats(withoutq);
        }
    }

    /*finds repeats of a word in the words array. 
    if the word is in the array add it to repeats.
    if the word isn't in the array it adds it to the array.
    */
    function findRepeats(word){
        //loop through words
        for(let z = 0; z < words.length; z++){
            // console.log(words[z].toLowerCase(), word.toLowerCase(), words[z].toLowerCase() === word.toLowerCase());
            if(words[z].toLowerCase() === word.toLowerCase()){
                repeats.push(words[z]);
                return
            }
        }
        words.push(word);
        return
    }

    console.log(repeats)
}