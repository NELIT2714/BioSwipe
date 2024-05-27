<script setup>

</script>

<template>
	<header>
		<nav>
			<div class="logo">
				<router-link :to="{name: 'Main'}">BioSwipe</router-link>
			</div>
			<div>
				<ul class="nav-links">
					<li><router-link :to="{name: 'Main'}">Główna</router-link></li>
					<li><router-link :to="{name: 'About'}">O nas</router-link></li>
				</ul>
			</div>
		</nav>
	</header>
	<router-view/>
</template>

<style scoped>
header {
	background-color: #191919;
	display: flex;
	justify-content: center;
	padding: 1rem 0;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 60rem;

}

.logo {

    font-size: 15pt;
    font-weight: 700;
}
.logo > a { color: white; }

.nav-links {
	display: flex;
	gap: 3rem;
}
.nav-links > li > a { color: white; }
</style>