$(function() {
    $('#getStat').click(function() {

        $.ajax({
            url: '/getStats',
            type: 'GET',
            success: function(responce) {
                console.log(responce);
                var tuples = [];
                $.each(responce, function(key, value) {
                    tuples.push([key, value]);
                });

                tuples.sort(function(a, b) {
                    a = a[1];
                    b = b[1];

                    return a < b ? -1 : (a > b ? 1 : 0);
                });

                for (var i = 0; i < tuples.length; i++) {
                    var key = tuples[i][0];
                    var value = tuples[i][1];

                    $( "#container" ).prepend("<p>" + key + ": " + value + "</p>");
                }

                var time = new Date();
                var year = time.getFullYear();
                var month = time.getMonth()+1;
                var date1 = time.getDate();
                var hour = time.getHours();
                var minutes = time.getMinutes();
                var seconds = time.getSeconds();
                $( "#container" ).prepend("<p>" + "Time "+  year + "-" + month+"-"+date1+" "+hour+":"+minutes+":"+seconds + "</p>");

            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
