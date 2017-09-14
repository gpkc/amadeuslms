$(function () {
	var locale = $("body").data('lang');

	if (!$("#sidebar-menu-div").children().length > 0) {
		//$("#sidebar-menu-div").remove();
		$("#page_content").switchClass('col-md-11', 'col-md-12', 0);
		$("#page_content").switchClass('col-lg-11', 'col-lg-12', 0);
	}
	
	$('.datetime-picker').datetimepicker({
		locale: locale
	});

	$('.date-picker').datetimepicker({
		locale: locale,
		format: 'L'
	});

	$('.text_wysiwyg').summernote({
	    height: 200,
	    lang: new_lang,
	    disableDragAndDrop: true,
	});

	$('[data-toggle="tooltip"]').tooltip({
		trigger: 'hover'
	});

	//Dropdown menu collapse
	$('.dropdown-accordion').on('click', 'a[data-toggle="collapse"]', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $($(this).data('parent')).find('.panel-collapse.in').collapse('hide');
        $($(this).attr('href')).collapse('show');
    });
});

var change_language = {
	post: function(url, language){
		$.post(url, language ,function(data){
				window.location.href= window.location.href;
		});
	}
}
