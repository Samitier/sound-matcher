<template>
	<div id="app">
		<SearchSelector/>
		<MatchList/>
	</div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import { Action } from "vuex-class"
import SearchSelector from "./components/search-selector.vue"
import MatchList from "./components/match-list.vue"

@Component({
	components: { SearchSelector, MatchList }
})
export default class App extends Vue {

	@Action fetchSearches: () => any

	async mounted() {
		this.fetchSearches()
	}
}
</script>

<style lang="stylus">
@import "./styles"

#app
	text-align center
	padding 2em
	max-width 500px
	margin auto

</style>
