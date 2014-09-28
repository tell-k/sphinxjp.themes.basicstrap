$(document).ready(function(){

  // Inline code styles to Bootstrap style.
  $('tt.docutils.literal').not(".xref").each(function (i, e) {
    // ignore references
    if (!$(e).parent().hasClass("reference")) {
      $(e).replaceWith(function () {
        return $("<code />").html($(this).html());
      });
  }});

  /*
   * Scroll the window to avoid the topnav bar
   * https://github.com/twitter/bootstrap/issues/1768
   */
  if ($(".navbar.navbar-fixed-top").length > 0) {
    // var navHeight = $(".navbar").height(),
    var navHeight = 40,
      shiftWindow = function() { scrollBy(0, -navHeight - 10); };
    if (location.hash) {
      setTimeout(shiftWindow, 1);
    }
    window.addEventListener("hashchange", shiftWindow);
  }

  /*
   * for QuickPreviewModal
   */
  if($.cookie('inner_theme')) {
      var bootstrap_version = $("#bootstrap-version").html();
      $("#current-theme").attr({href: "_static/css/bootstrap" + bootstrap_version + "/" +$.cookie('inner_theme') + ".css"})
      $("#current-adjust-theme").attr({href: "_static/css/adjust_theme/" + $.cookie('inner_theme') + ".css"})
      $('#select-theme').val($.cookie('inner_theme'));
  }
  if($.cookie('header_inverse')) {
      $("#navbar-top").removeClass("navbar-default");
      $("#navbar-top").removeClass("navbar-inverse");
      $("#navbar-top").addClass("navbar-" + $.cookie('header_inverse'));

      if ($.cookie('header_inverse') == 'inverse') {
        $('#select-header-inverse').attr('checked', true);
      }
  }
  if($.cookie('relbar_inverse')) {
      $("#navbar-related").removeClass("navbar-default");
      $("#navbar-related").removeClass("navbar-inverse");
      $("#navbar-related").addClass("navbar-" + $.cookie('relbar_inverse'));
      if ($.cookie('relbar_inverse') == 'inverse') {
        $('#select-relbar-inverse').attr('checked', true);
      }
  }
  $("#select-theme").change(function(e){
      e.preventDefault();
      var bootstrap_version = $("#bootstrap-version").html();
      var theme;
      $("#select-theme option:selected").each(function () {
          theme = $(this).val();
      });
      if (theme == '') {
          $("#current-theme").attr({href: "_static/css/bootstrap" + bootstrap_version + "/bootstrap.min.css"})
          $("#current-adjust-theme").attr({href: ""})
          $.cookie('inner_theme', theme, {expires: 1, path: '/'});
          return
      }
      $("#current-theme").attr({href: "_static/css/bootstrap" + bootstrap_version + "/" + theme + ".css"})
      $("#current-adjust-theme").attr({href: "_static/css/adjust_theme/" + theme + ".css"})
      $.cookie('inner_theme', theme, {expires: 1, path: '/'});
  });
  $("#select-header-inverse").change(function(e){
      var inverse = $('#select-header-inverse').prop("checked");
      var inverse_type = (inverse) ? 'inverse' : 'default';

      $("#navbar-top").removeClass("navbar-default");
      $("#navbar-top").removeClass("navbar-inverse");
      $("#navbar-top").addClass("navbar-" + inverse_type);
      $.cookie('header_inverse', inverse_type, {expires: 1, path: '/'});

  });
  $("#select-relbar-inverse").change(function(e){
      var inverse = $('#select-relbar-inverse').prop("checked");
      var inverse_type = (inverse) ? 'inverse' : 'default';

      $("#navbar-related").removeClass("navbar-default");
      $("#navbar-related").removeClass("navbar-inverse");
      $("#navbar-related").addClass("navbar-" + inverse_type);
      $.cookie('relbar_inverse', inverse_type, {expires: 1, path: '/'});
  });

});
