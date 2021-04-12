module.exports = {
	purge: [],
	darkMode: false, // or 'media' or 'class'
	theme: {
		extend: {
			outline: {
				black: '2px solid #000000',
			},
			colors: {
				transparent: 'transparent',
				current: 'currentColor',
				blue: {
					'pale': '#B7CADB',
					'light': '#4A7195',
					'royal': '#005fa9',
					'navy': '#0e355a',
				},
				red: '#a40046',
				'abiomed-teal': {
					'pale': '#cbf9fc',
					'light': '#8AC4C8',
					DEFAULT: '#309fa7',
					'dark': '#17656b',
				},
				gold: '#fdb913',
				silver: '#297081',
			},
		},
	},
	variants: {
		backgroundColor: ['responsive', 'hover', 'focus', 'active', 'disabled'],
    	textColor: ['responsive', 'hover', 'focus', 'active', 'disabled'],
		opacity: ['responsive', 'hover', 'focus', 'active', 'disabled'],
	},
	plugins: [
		require('tailwindcss-textshadow')
	],
}
