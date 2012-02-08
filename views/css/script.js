function showHideTab(text)
{
    donorsty = document.getElementById("donor_div");
    recepsty = document.getElementById("recep_div");
    catsty = document.getElementById("category_div");
    donationsty = document.getElementById("donation_div");

    donorsty.style.display=(text == "donor_div")?"inherit":"none";
    recepsty.style.display=(text == "recep_div")?"inherit":"none";
    donationsty.style.display=(text == "donation_div")?"inherit":"none";
    catsty.style.display=(text == "category_div")?"inherit":"none";
}