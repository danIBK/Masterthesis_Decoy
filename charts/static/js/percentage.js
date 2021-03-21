// Formel für Eingabe in Anteil in €
// A -> B and B->

function updateValueA(val) {
    document.getElementById('asset_b').value= 10000-val;
    document.getElementById('percentage_rf_text').value= val/10000*100;
    document.getElementById('percentage_rf_range').value=val/10000*100;
    document.getElementById('percentage_market_text').value= 100-(val/10000*100);
    }
function updateValueB(val){
    document.getElementById('asset_a').value = 10000-val;
    document.getElementById('percentage_market_text').value= val/10000*100;
    document.getElementById('percentage_rf_range').value=100-(val/10000*100);
    document.getElementById('percentage_rf_text').value= 100-(val/10000*100);
    }
// Update Risk Free function
// for percentage_rf_range and
// for percentage_rf_text
// WENN RANGE GEÄNDERT WIRD WIRD TEXT ANGEPASST
function updatepercentage_rf_text(val) {
    document.getElementById('asset_a').value=val*100;
    document.getElementById('percentage_rf_range').value= val;
    document.getElementById('percentage_market_text').value=100-val;
    document.getElementById('asset_b').value= 10000-val*100;

    }
function updatepercentage_rf_range(val) {
    document.getElementById('asset_a').value=val*100;
    document.getElementById('percentage_rf_text').value= val;
    document.getElementById('percentage_market_text').value=100-val;
    document.getElementById('asset_b').value= 10000-val*100;
    }
    // Validation RF text
// WENN WERT nicht in Range auf min/max setzen
function validateRFInput(){
    if (parseFloat(document.getElementById('percentage_rf_text').value) < 0) {
        document.getElementById('percentage_rf_text').value = 0;
    }
    if (parseFloat(document.getElementById('percentage_rf_text').value) > 100) {
        document.getElementById('percentage_rf_text').value = 100;
        }
    }
// Update Same function
// for market_rf_range and
// for market_rf_text
// WENN RANGE GEÄNDERT WIRD WIRD TEXT ANGEPASST und Andersrum

function updatepercentage_market_text(val) {
    document.getElementById('asset_a').value=10000-val*100;
    document.getElementById('percentage_rf_text').value=100-val;
    document.getElementById('percentage_rf_range').value= 100-val;
    document.getElementById('asset_b').value= val*100;
}
      function updatepercentage_market_range(val) {
          document.getElementById('percentage_market_range').value=val;
      }

    // Validation Market text
function validateMarketInput(){
    if (parseFloat(document.getElementById('percentage_market_text').value) < 0) {
        document.getElementById('percentage_market_text').value = 0;
    }
    if (parseFloat(document.getElementById('percentage_market_text').value) > 100) {
        document.getElementById('percentage_market_text').value = 100;
        }
    if (parseFloat(document.getElementById('asset_b').value) < 0) {
        document.getElementById('asset_b').value = 0;
        }
    if (parseFloat(document.getElementById('asset_b').value) > 10000) {
        document.getElementById('asset_b').value = 10000;
        }

    }
