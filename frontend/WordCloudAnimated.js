!function(){
    var WordCloudAnimated = {};

    WordCloudAnimated.drawWordCloud = function (){
        //var fill = d3.scale.category20();
        var selector = "#forCloud";

        var node  = d3.select(selector).node();
        var rectBoxInfo = node.getBoundingClientRect();
        var width = rectBoxInfo.width; //$(document).width();
        var height = rectBoxInfo.height; //$(document).height();

        var fill = function (i) {
            if(i%3 == 0) {
                return donutColors.negative;
            } else if(i%3 == 1) {
                return donutColors.neutral;
            } else {
                return donutColors.positive;
            }
        };

        //Construct the word cloud's SVG element
        var svg = d3.select(selector).append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + [width >> 1, height >> 1] + ")");


        //Draw the word cloud
        function draw(words) {
            var cloud = svg.selectAll("g text")
                            .data(words, function(d) { return d.text; })

            //Entering words
            cloud.enter()
                .append("text")
                .style("font-family", "Impact")
                .style("fill", function(d, i) { return fill(d.sent); })
                .attr("text-anchor", "middle")
                .attr('font-size', 1)
                .text(function(d) { return d.text; });

            //Entering and existing words
            cloud
                .transition()
                    .duration(600)
                    .style("font-size", function(d) { return d.size + "px"; })
                    .attr("transform", function(d) {
                        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .style("fill-opacity", 1);

            //Exiting words
            cloud.exit()
                .transition()
                    .duration(200)
                    .style('fill-opacity', 1e-6)
                    .attr('font-size', 1)
                    .remove();
        }


        //Use the module pattern to encapsulate the visualisation code. We'll
        // expose only the parts that need to be public.
        WordCloudAnimated.currentWordCloud =  {

            //Recompute the word cloud for a new set of words. This method will
            // asycnhronously call draw when the layout has been computed.
            //The outside world will need to call this function, so make it part
            // of the wordCloud return value.
            update: function(words) {

                var selector = "#forCloud";

                var node  = d3.select(selector).node();
                var rectBoxInfo = node.getBoundingClientRect();
                var width = rectBoxInfo.width; //$(document).width();
                var height = rectBoxInfo.height; //$(document).height();

                var xScale = d3.scale.linear()
                    .domain([0, d3.max(words, function(d) {
                        return d.size;
                    })
                    ])
                    .range([10,100]);
                d3.layout.cloud().size([width, height])
                    .words(words)
                    .padding(5)
                    .rotate(function() { return ~~(Math.random() * 2) * 90; })
                    .font("Impact")
                    .fontSize(function(d) { return xScale(d.size); })
                    .on("end", draw)
                    .start();

                //$(selector).focus();
                $(window).scrollTop($(selector).position().top);
            }
        }
    }
    WordCloudAnimated.updateWordCloud = function (word_count){
        var word_count_arr = [];
        for (var key in word_count) {
            word_count_arr.push({"text":key,"size":word_count[key].freq,"sent":word_count[key].sent });
        }
        WordCloudAnimated.currentWordCloud.update(word_count_arr);
    }

    this.WordCloudAnimated = WordCloudAnimated;
}();