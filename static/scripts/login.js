function showPassword() 
{
    var senhaInput = document.getElementById("password");
    if (senhaInput.type === "password") {
        senhaInput.type = "text";
    } else {
        senhaInput.type = "password";
    }
}