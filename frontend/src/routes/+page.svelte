<script>
	import { readable } from 'svelte/store';
	import { degrees, description, location, icon, fn } from "./stores";
    import Weather from './Weather.svelte';
	
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

	async function handleClick(city) {

		const testData = {
			temp: 19,
			location: city,
			description: "Broken Clouds",
			icon: "&#9728",
		}
		
		fn.set(0);

		try {
			const response = await fetch('./fakepage');
			if (!response.ok) {
				throw new Error('Network response was not OK');
			}
			return await response.text();

		} catch (error) {
			//console.error('There has been a problem with your fetch operation:', error);
			setReport(testData);
			fn.set(1);

			return testData;
		}
		
	}
	
	function setReport(data) {
		degrees.set(data.temp);
		description.set(data.description);
		location.set(data.location);
		icon.set(data.icon);
	}

	//	Background of the sky-
	//	Full page BG
	//	Bottom 50% cover

	import logo from '$lib/images/gwai.webp';

	const recent = ['London', 'New York', 'Tokyo'];

</script>

<header>
	
	<p><img class='logo-img' src={logo} alt="GreatWave AI" /> | No Nonsense, Just Weather</p>
</header>

<Weather />

<div>
	<p>
		Location:
		{#each recent as location, i}
			<button on:click={() => handleClick(location) }>{location}</button>
		{/each}
	</p>
</div>

<footer>
	<p>{formatter.format($time)}</p>
</footer>

<style>
	header {
		height: 2vh;
		color: #fff;
	}
	.logo-img {
		display: inline-block;
		height: 100%;
		max-height: 50px;
	}

	footer {
		height: 4vh;
	}

</style>
