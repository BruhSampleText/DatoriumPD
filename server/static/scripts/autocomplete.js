// somewhat taken from: https://www.w3schools.com/howto/howto_js_autocomplete.asp

/**
 * @argument {HTMLInputElement} inputField
 */

var tags = []

const bind_tag_autocomplete = ( inputField ) => {
	/**@type {HTMLDivElement} */
	const autocomplete_result_list = document.createElement( "div" )
	autocomplete_result_list.setAttribute( "class", "autocomplete-items" )
	inputField.parentElement.append( autocomplete_result_list )

	fetch( "../get/tags" )
		.then( response => response.json() )
		.then( data => { tags = data } )

	const clear_suggestions = () => {
		while( autocomplete_result_list.firstChild ) {
			autocomplete_result_list.removeChild( autocomplete_result_list.lastChild )
		}
	}

	inputField.addEventListener( "keyup", event => {

		/**@type {string[]} */
		let input_array = inputField.value.split( " " )

		/**@type {string} */
		let input = input_array.pop().toLowerCase()

		clear_suggestions()

		for ( let suggestion of tags ) {
			if ( suggestion.startsWith( input ) ) {
				const suggestion_button = document.createElement( "div" )
				suggestion_button.innerHTML = `<b>${ suggestion.substring( 0, input.length ) }</b>${ suggestion.substring( input.length ) }`
				suggestion_button.onclick = () => {
					input_array.push( suggestion )

					let str = ""
					input_array.forEach( entry => { str += " " + entry } )
					inputField.value = str.trimStart()

					clear_suggestions()
				}

				autocomplete_result_list.append( suggestion_button )
			}
		}

	} )

	document.addEventListener( "click", clear_suggestions )

}