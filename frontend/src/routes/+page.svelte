<script>
	import { readable } from 'svelte/store';

	const location = "London, UK";

	const time = readable(new Date(), function start(set) {
		const interval = setInterval(() => {
			set(new Date());
		}, 1000);

		return function stop() {
			clearInterval(interval);
		};
	});

	const formatter = new Intl.DateTimeFormat(
		'en',
		{
			hour12: true,
			hour: 'numeric',
			minute: '2-digit',
			second: '2-digit'
		}
	);

	//	Background of the sky-
	//	Full page BG
	//	Bottom 50% cover
	

</script>

<header>
	<p>Logo | No Nonsense, Just Weather</p>
</header>

<section>
	<div id='weather-holder'>
		
		<h1>{location}</h1>

		<div id='deg-holder'>
			<span id='deg-number'>20<span id='deg-symbol'>&deg;C</span></span>
		</div>
		<div id='description'>
			Cloudy
		</div>

		<div id='weather-symbol'>
		    <!--&#9729;-->
			&#9728; <!-- This is the HTML entity for the sun symbol -->
		</div>

	</div>
</section>
<div>
	<p>
		Location:
		<b>New York</b>
		<b>Tokyo</b>
	</p>
</div>

<footer>
	<p>{formatter.format($time)}</p>
</footer>

<style>
	header {
		height: 5vh;
	}

	section {
		height: 80vh;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	footer {
		height: 5vh;
	}

	#weather-holder {
		text-align: center;
	}
	#deg-number {
		font-size: 5rem;
	}
	#deg-symbol {
	    font-size: 2rem;
	    vertical-align: super;
	}
	#description {
		text-transform: uppercase;
		letter-spacing: 2px;
	}

	#weather-symbol {
		position: absolute;
		top: 35%;
		left: 50%;
		transform: translate(-50%, -50%);
		opacity: .5;
		font-size: 13rem;
	}

</style>
