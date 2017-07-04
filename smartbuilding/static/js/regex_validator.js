function validatePasswordRegex(p) {
    var newPassword = p.value;
    console.log(newPassword.length + ' ' + newPassword + ' ' + newPassword.search(/[a-z]/) + ' ' + newPassword.search(/[0-9]/));
    if(newPassword.length < 8){
        p.setCustomValidity("muy corta");
    }else if (newPassword.search(/[a-zA-Z]/) < 0) {
        p.setCustomValidity("Your password must contain at least one letter.");
    }else if (newPassword.search(/[0-9]/) < 0) {
        p.setCustomValidity("Your password must contain at least one digit.");
    } else{
       p.setCustomValidity("");
    }
}