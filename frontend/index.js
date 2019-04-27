$( document ).ready(function() {
    console.log( "ready!" );
    donutColors = {
        "positive":"#4285f4",
        "negative":"#db4437",
        "neutral":"#f4b400"
    };

    BubbleChart.loadChart();
    // $.getJSON("../data/sample_reduced_word_count.json",function(json) {
    //     //word_count = json;
    //     console.log(json); // this will show the info it in firebug console
    //     WordCloud.drawWordCloud(json);
    // });
    // LineChart.createLine();
    pieChart.makePie("",0);
});