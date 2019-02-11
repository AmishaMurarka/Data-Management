// JavaScript source code
function add_cust_validate() {
    var f_n, l_n, addr, city, c1, c2, email;
    f_n = document.getElementById("f_n");
    l_n = document.getElementById("l_n");
    addr = document.getElementById("addr");
    city = document.getElementById("city");
    c1 = document.getElementById("c1");
    c2 = document.getElementById("c2");
    email = document.getElementById("email");
    if (isAlpha(f_n)) {
        if (isAlpha(l_n)) {
            if (isAlphaNum(addr)) {
                if (isAlpha(city)) {
                    if (isContact(c1)) {
                        if (isContact(c2)) {
                            if (isEmail(email)) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

function del_cust_validate() {
    var cus_name;
    cus_name = document.getElementById("cus_name");
    if (isAlpha(cus_name)) {
        return true;
    }
    return false;
}

function isAlpha(element) {
    var exp = /^[a-zA-z]+$/;
    if (element.value.match(exp)) {
        return true;
    }
    else {
        alert("Field must contain a alphabetical value..");
        element.focus();
        return false;
    }
}


function isAlphaNum(element) {
    var exp = /^[0-9a-zA-z]+$/;
    if (element.value.match(exp)) {
        return true;
    }
    else {
        alert("Field must contain a numeric value..");
        element.focus();
        return false;
    }
}

function inrange(element) {
    var val = element.value;
    if (val >= 1 || val <= 5) {
        return true;
    }
    else {
        alert("Rating must be between the range 1 and 5..");
        element.focus();
        return false;
    }
}

function isEmail(element) {
    var exp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (element.value.match(exp)) {
        return true;
    }
    else {
        alert("Please enter an appropriate email..");
        element.focus();
        return false;
    }
}

function isContact(element) {
    if (element.value.length == 10) {
        return true;
    }
    else {
        alert("Please enter an appropriate contact..");
        element.focus();
        return false;
    }
}
