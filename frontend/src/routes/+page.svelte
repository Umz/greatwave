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

	async function selectLocation(city) {

		const testData = {
			temp: 19,
			location: city,
			description: "Clear Skies",
			icon: "04d",
		}
		
		fn.set(0);

		try {

			const url = `http://127.0.0.1:5000/?city=${city}`;
			const response = await fetch(url);
			if (!response.ok) {
				throw new Error('Network response was not OK');
			}

			const data = await response.json();
			setReport(data);
			fn.set(1);

		} catch (error) {
			setReport(testData);
			fn.set(-1);
		}

		return true;
	}
	
	function setReport(data) {
		degrees.set(data.temp);
		description.set(data.description);
		location.set(data.location);
		icon.set(data.icon);
	}

	import logo from '$lib/images/gwai.webp';
	const recent = ['London', 'New York', 'Tokyo'];

</script>

<header>
	<p class='header-logo'>
		<img class='logo-img' src={logo} alt="GreatWave AI" /> | Just Weather
	</p>
</header>

<Weather />

<footer>
	<div class='content'>
		<p class='city city-title'>
			City
		</p>
		<p class='city'>
			{#each recent as location, i}
				<button class='button-89' on:click={() => selectLocation(location) }>{location}</button>
			{/each}
		</p>
		<p class='time-text'>{formatter.format($time)}</p>
	</div>
</footer>

<style>
	.content {
		width: 90%;
		margin: auto;
	}

	header {
		width: 100%;
		margin: 0;
		color: #fff;
	}

	.logo-img {
		display: inline-block;
		height: 100%;
		max-height: 40px;
	}

	footer {
		width: 100%;
		position: absolute;
		bottom: 0;
		left: 0;
		
		bottom: 0;
		
		background-color: rgba(255, 255, 255, .0);
	}

	.city {
		margin: 0;
		text-align: center;
	}

	.city-title {
		font-weight: 900;
		text-transform: uppercase;
		letter-spacing: 4px;
		transform: translate(0, -.75rem);
	}

	.time-text {
		font-size: .8rem;
		font-weight: 600;
	}

	button {
		margin: 0 5px;
	}
	
	/*  White box button */
	.button-30 {
		align-items: center;
		appearance: none;
		background-color: #FCFCFD;
		border-radius: 4px;
		border-width: 0;
		box-shadow: rgba(45, 35, 66, 0.4) 0 2px 2px,rgba(45, 35, 66, 0.3) 0 3px 6px -3px,#D6D6E7 0 -3px 0 inset;
		box-sizing: border-box;
		color: #36395A;
		cursor: pointer;
		display: inline-flex;
		font-family: "JetBrains Mono",monospace;
		height: 40px;
		justify-content: center;
		line-height: 1;
		list-style: none;
		overflow: hidden;
		padding-left: 12px;
		padding-right: 12px;
		position: relative;
		text-align: left;
		text-decoration: none;
		transition: box-shadow .15s,transform .15s;
		user-select: none;
		-webkit-user-select: none;
		touch-action: manipulation;
		white-space: nowrap;
		will-change: box-shadow,transform;
		font-size: 18px;
	}

	.button-30:focus {
		box-shadow: #D6D6E7 0 0 0 1.5px inset, rgba(45, 35, 66, 0.4) 0 2px 4px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
	}

	.button-30:hover {
		box-shadow: rgba(45, 35, 66, 0.4) 0 4px 8px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
		transform: translateY(-4px);
	}

	.button-30:active {
		box-shadow: #D6D6E7 0 3px 7px inset;
		transform: translateY(2px);
	}

	/* Black box button */
	.button-89 {
		--b: 1px;   /* border thickness */
		--s: .45em; /* size of the corner */
		--color: #373B44;
		
		padding: calc(.5em + var(--s)) calc(.9em + var(--s));
		color: var(--color);
		--_p: var(--s);
		background:
			conic-gradient(from 90deg at var(--b) var(--b),#0000 90deg,var(--color) 0)
			var(--_p) var(--_p)/calc(100% - var(--b) - 2*var(--_p)) calc(100% - var(--b) - 2*var(--_p));
		transition: .3s linear, color 0s, background-color 0s;
		outline: var(--b) solid #0000;
		outline-offset: .6em;

		border: 0;

		user-select: none;
		-webkit-user-select: none;
		touch-action: manipulation;
	}

	.button-89:hover,
	.button-89:focus-visible{
		--_p: 0px;
		outline-color: var(--color);
		outline-offset: .05em;
	}

	.button-89:active {
		background: var(--color);
		color: #fff;
	}
</style>