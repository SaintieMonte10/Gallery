$(document).ready(function(){

    $('.category-button').click(function(event) {
      event.preventDefault()
      var btn_value = $(this).text()
  
      $.ajax({
        'url': 'category/',
        'type': 'GET',
        'data': {
          category_name: btn_value
        },
        'success': function(resp) {
          $('.container-fluid').empty()
          $('.container-fluid').html(resp)
        },
  
      })
    })
    
    $('option').click(function() {
      if ($(this).is(':selected')) {
        option_value = $(this).text()
        $.ajax({
          'url': 'location/',
          'type': 'GET',
          'data': {
            location_name: option_value
          },
          'success': function(resp) {
            $('.container-fluid').empty()
            $('.container-fluid').html(resp)
          },
  
        })
      }
  
    })
  
  
  $('.my_image').click(function(){
      $('#myModal').css('display', "block")
      $("#modal-con").attr('src',$(this).attr('src'))
      $('#caption').html()= $(this).attr('alt')
  })
  
  $('button#details').click(function() {
  
    $('#modal-details').css('display', 'block')
  
    img_d = $(this).data("description");
  
    loc_d = $(this).data("location");
  
    cat_d = $(this).data("category");
  
    url_d = $(this).data("url")
  
    $(".oneone").text(img_d);
  
    $(".twotwo").text(loc_d);
  
    $(".threethree").text(cat_d);
  
    $(".fourfour").text(url);
    
  
  
  })
  
  $(".close").click(function() {
    $('#Modal_pic').css('display', "none");
    $('#modal-details').css('display', 'none')
  })
  })
  
  
  // function copyUrl() {
  //   /* Get the text field */
  //   var copyUrl = document.getElementById("myInput");
  
  //   /* Select the text field */
  //   copyUrl.select();
  
  //   /* Copy the text inside the text field */
  //   document.execCommand("copy");
  
  //   /* Alert the copied text */
  //   alert("Copied the url: " + copyUrl.value);
  // }
  
  
  
  function CopyFunction() {
    var CopyFunction = document.getElementById("myInput");
    CopyFunction.select();
    document.execCommand("copy");
    alert("Copied the text: " + CopyFunction.value);
  }