<script>
    import { fade, fly } from 'svelte/transition';
    import { degrees, description, location, icon, fn } from "./stores";

    let subDeg = 2;
    let subLoc = "London, UK";
    let subDesc = "Cold";
    let subIcon = "04d";

    let showLoading = true;
    let loading = "Loading...";
    let src = "http://openweathermap.org/img/w/04d.png";

    degrees.subscribe(v => subDeg = Math.round(v));
    description.subscribe(v => subDesc = v);
    location.subscribe(v => subLoc = v);
    icon.subscribe(v => subIcon = v);
    
    fn.subscribe(v => {
        if (v < 0) {
            loading = "Some errors occured.";
        }
        else if (v === 0) {
            loading = "Getting weather..";
        }
        else {
            //  Hack - Svelte is being unco-operative?
            const ele = document.getElementById('wsimg');
            if (ele) {
                ele.src = `https://openweathermap.org/img/wn/${subIcon}@2x.png`
            }
        }

        showLoading = v <= 0;
    });
    
</script>

{#if showLoading}
    
    <section id="loading-section" transition:fade>
        {loading}
    </section>

{:else}

    <section id="weather-section" transition:fly>
        <div id='weather-holder'>
            
            <h1>{subLoc}</h1>

            <div id='weather-symbol'>
                <img id='wsimg' {src} alt={subDesc} />
            </div>

            <div id='deg-holder'>
                <span id='deg-number'>{subDeg}<span id='deg-symbol'>&deg;C</span></span>
            </div>
            <div id='description'>
                <p>{subDesc}</p>
            </div>

        </div>
    </section>

{/if}

<style>
    section {
		height: 70vh;
		display: flex;
		justify-content: center;
		align-items: center;
	}
    #loading-section {
        text-align: center;
        text-transform: uppercase;
		letter-spacing: 2px;
    }

    #weather-holder {
        min-width: 260px;
        background-color: rgba(255, 255, 255, .3);
        padding: 25px;
        border: 3px solid white;
        border-radius: 20px;
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
		margin: 10px;
	}
    #wsimg {
        transform: scale(2);
    }
</style>