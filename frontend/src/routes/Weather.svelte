<script>
    import { fade } from 'svelte/transition';
    import { degrees, description, location, icon, fn } from "./stores";

    let subDeg = 2;
    let subLoc = "London, UK";
    let subDesc = "Cold";
    let subIcon = "&#9728";

    let showLoading = true;
    let loading = "Loading...";

    degrees.subscribe(v => subDeg = v);
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
        showLoading = v <= 0;
    });
    
    // &#9729;
	// &#9728;

</script>

{#if showLoading}
    
    <section id="loading-section" transition:fade>
        {loading}
    </section>

{:else}

    <section id="weather-section" transition:fade>
        <div id='weather-holder'>
            
            <h1>{subLoc}</h1>

            <div id='deg-holder'>
                <span id='deg-number'>{subDeg}<span id='deg-symbol'>&deg;C</span></span>
            </div>
            <div id='description'>
                <p>{subDesc}</p>
            </div>

            <div id='weather-symbol'>
                {@html subIcon}
            </div>

        </div>
    </section>

{/if}

<style>
    section {
		height: 80vh;
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