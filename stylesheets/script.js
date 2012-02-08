function showHideTab(text)
{
    donorsty = document.getElementById("donor_div");
    recepsty = document.getElementById("recep_div");
    catsty = document.getElementById("category_div");
    donationsty = document.getElementById("donation_div");
    vdonorssty = document.getElementById("vdonors_div");

    donorsty.style.display=(text == "donor_div")?"inherit":"none";
    recepsty.style.display=(text == "recep_div")?"inherit":"none";
    donationsty.style.display=(text == "donation_div")?"inherit":"none";
    catsty.style.display=(text == "category_div")?"inherit":"none";
    vdonorssty.style.display=(text == "vdonors_div")?"inherit":"none";

    donorli = document.getElementById("donor_div_li");
    recepli = document.getElementById("recep_div_li");
    catli = document.getElementById("category_div_li");
    donationli = document.getElementById("donation_div_li");
    vdonorsli = document.getElementById("vdonors_div_li");

    donorli.setAttribute("class", (text == "donor_div")?"current":"bkgrnd");
    recepli.setAttribute("class", (text == "recep_div")?"current":"bkgrnd");
    donationli.setAttribute("class", (text == "donation_div")?"current":"bkgrnd");
    catli.setAttribute("class", (text == "category_div")?"current":"bkgrnd");
    vdonorsli.setAttribute("class", (text == "vdonors_div")?"current":"bkgrnd");

}