$("#log_in_header").mouseover(function() { $(this).css("fontStyle", "italic") });
$("#log_in_header").mouseout(function() { $(this).css("fontStyle", "normal") });

$(function(){
     $('form').on('button_addon2', function(e){
         e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: $(this).attr('method'),
             success: function(data){ $('#target').html(data) }
         });
     });
});