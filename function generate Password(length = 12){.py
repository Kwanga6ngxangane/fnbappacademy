function generate Password(length = 12){
const lowercase = 'abcdefghijklmnopqrstuvxyz' ;
const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVXYZ' ;
const numbers = '0123456789' ;
const symbols = '!@#$%^&*()_+{}[]|\' ;

const allchars = lowercase + uppercase + numbers + symbols;

let password = '';
for(let i =0; i < length; i++){
    const randonIndex = math.floor(math.random() *allchars.length);
    password += allchars[randomIndex];
}
return password;
}

console.log('password generator');
for (let i = 0; i < 5; i++){
    console.log(`${i+i}.${generatePassword()}`);
}

console.log("======================");