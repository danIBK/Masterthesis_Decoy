// Formel für Eingabe in Anteil in €
// A -> B and B->

function updateRF(val) {
    document.getElementById('percentage_RF_text').value= val/10000*100;
    }
function updateMFA(val){
    document.getElementById('percentage_MFA_text').value = val/10000*100;
    }
function updateMFB(val){
    document.getElementById('percentage_MFB_text').value = val/10000*100;
    }
// Update Risk Free function
// for percentage_rf_range and
// for percentage_rf_text
// Anteil % -> Anteil €
function updatepercentage_RF_text(val) {
    document.getElementById('RF').value=val*100;
    }
function updatepercentage_MFA_text(val) {
    document.getElementById('MFA').value=val*100;
    }
function updatepercentage_MFB_text(val) {
    document.getElementById('MFB').value=val*100;
    }

// Update Same function
// for market_rf_range and
// for market_rf_text
// WENN RANGE GEÄNDERT WIRD WIRD TEXT ANGEPASST und Andersrum

// function updatepercentage_market_text(val) {
//     document.getElementById('asset_a').value=10000-val*100;
//     document.getElementById('percentage_rf_text').value=100-val;
//     document.getElementById('percentage_rf_range').value= 100-val;
//     document.getElementById('asset_b').value= val*100;
// }
    // Validation RF
// WENN WERT nicht in Range auf min/max setzen
function validateRF(){
    if (parseFloat(document.getElementById('percentage_RF_text').value) < 0) {
        document.getElementById('percentage_RF_text').value = 0;
    }
    if (parseFloat(document.getElementById('percentage_RF_text').value) > 100) {
        document.getElementById('percentage_RF_text').value = 100;
        }
    if (parseFloat(document.getElementById('RF').value) < 0) {
        document.getElementById('RF').value = 0;
    }
    if (parseFloat(document.getElementById('RF').value) > 10000) {
        document.getElementById('RF').value = 10000;
        }
    }

    // Validation Marketfonds A
function validateMFA(){
    if (parseFloat(document.getElementById('percentage_MFA_text').value) < 0) {
        document.getElementById('percentage_MFA_text').value = 0;
    }
    if (parseFloat(document.getElementById('percentage_MFA_text').value) > 100) {
        document.getElementById('percentage_MFA_text').value = 100;
        }
    if (parseFloat(document.getElementById('MFA').value) < 0) {
        document.getElementById('MFA').value = 0;
        }
    if (parseFloat(document.getElementById('MFA').value) > 10000) {
        document.getElementById('MFA').value = 10000;
        }
    }
    // Validation Marketfonds B
function validateMFB() {
    if (parseFloat(document.getElementById('percentage_MFB_text').value) < 0) {
        document.getElementById('percentage_MFB_text').value = 0;
    }
    if (parseFloat(document.getElementById('percentage_MFB_text').value) > 100) {
        document.getElementById('percentage_MFB_text').value = 100;
    }
    if (parseFloat(document.getElementById('MFB').value) < 0) {
        document.getElementById('MFB').value = 0;
    }
    if (parseFloat(document.getElementById('MFB').value) > 10000) {
        document.getElementById('MFB').value = 10000;
    }
}


    function updateSuM() {
        var rf = parseFloat(document.getElementById('percentage_RF_text').value)
        var mfa = parseFloat(document.getElementById('percentage_MFA_text').value)
        var mfb = parseFloat(document.getElementById('percentage_MFB_text').value)


        if (isNaN(rf) || isNaN(mfa) || isNaN(mfb))
        {
            if (isNaN(rf) && isNaN(mfa)) {
                document.getElementById('sum_percentage').value = mfb.toFixed(2)
            }
            else {
                if (isNaN(rf) && isNaN(mfb)) {
                    document.getElementById('sum_percentage').value = mfa.toFixed(2)
                }
                else
                    { if (isNaN(mfa) && isNaN(mfb)) {
                        document.getElementById('sum_percentage').value = rf.toFixed(2)
                    }
                    else {
                        if (isNaN(rf)) {
                            document.getElementById('sum_percentage').value = (mfa +mfb).toFixed(2)
                        }
                        else {
                            if (isNaN(mfa)) {
                                document.getElementById('sum_percentage').value = (rf +mfb).toFixed(2)
                            }
                            else {
                                if (isNaN(mfb)) {
                                    document.getElementById('sum_percentage').value = (rf + mfa).toFixed(2)
                                }
                            }
                        }
                    }
                     }
                }
        }
        else {
            document.getElementById('sum_percentage').value = (rf + mfa + mfb).toFixed(2)
                // parseFloat(document.getElementById('percentage_RF_text').value) +
                // parseFloat(document.getElementById('percentage_MFA_text').value) +
                // parseFloat(document.getElementById('percentage_MFB_text').value);
            }
    }


