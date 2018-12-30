$( '.nav-link' ).click (function () {
	console.log("custoM");
	$( '.nav-link' ).find( 'li.active' ).removeClass( 'active' );
	$( this ).parent( 'li' ).addClass( 'active' );
});