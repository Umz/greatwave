import { writable } from 'svelte/store';

export const degrees = writable(0);
export const description = writable("");
export const location = writable("");
export const icon = writable("");

export const fn = writable(0);