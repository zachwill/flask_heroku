var resize = function(){
    $('.sizing').each(function(){
        var self = $(this),
            width = self.width()
        self.height(width)
    })
}

$(window).resize(resize)
$(document).ready(resize)
