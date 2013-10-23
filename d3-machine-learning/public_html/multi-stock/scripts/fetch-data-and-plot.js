
// configs and tools
var stock_url = 'http://127.0.0.1:5000/closing-price?ticker=goog';

function getRemote() {
    return $.ajax({
        type: "GET",
        url: stock_url,
        async: false,
    }).responseText;
}



console.log('starting to fetch stock data');

//
var stock_data = getRemote();
console.log(stock_data[0]);
console.log();
console.log();


console.log('finished fetching stock data');

console.log('configuring time-series plot');



console.log('populating time-series plot');