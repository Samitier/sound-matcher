<template>
	<section>
		<div ref="selectedSearch" class="selected-search">
			<div v-if="selectedSearch" class="ellipsis">
				<RecordingDetail :recording="selectedSearch" :selectable="true"/>
			</div>
			<div v-else class="placeholder ellipsis">
				Select an input report to see its candidates
			</div>
			<i class="material-icons caret">keyboard_arrow_down</i>
		</div>
		<div class="searches-list" v-if="showList">
			<div 
				v-for="search in searches"
				:key="search.id"
				@click="selectSearch(search)"
			>
				<RecordingDetail :recording="search" :selectable="true"/>
			</div>
		</div>
	</section>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import { State, Action } from "vuex-class"
import Recording from "@/models/recording.model"
import RecordingDetail from "@/components/recording-detail.vue"

@Component({
	components: { RecordingDetail }
})
export default class SearchSelector extends Vue {

	@State selectedSearch: Recording
	@State searches: Recording[]
	@Action selectSearch: (s: Recording) => any

	showList: boolean = false

	mounted() {
		window.addEventListener("click", this.onToggleShowList)
	}

	beforeDestroy() {
		window.removeEventListener("click", this.onToggleShowList)
	}

	// Opening the list when the user clicks the selectedSearch & closing
	// it when they click anywhere else.
	onToggleShowList({ target }: Event) {
		this.showList = (this.$refs.selectedSearch as any).contains(target)
	}
}
</script>

<style lang="stylus" scoped>
	.selected-search
		background #eee
		border-radius 5px
		padding 1.2em
		text-align left
		position relative
		cursor pointer
		.placeholder
			color #636c72
		>div
			padding-right 1.3em
	.caret
		position absolute
		right .3em
		top 50%
		transform translateY(-50%)
		font-size 38px
		color #292b2c
	.searches-list
		background #FBFBFB
		text-align left
		padding .7em 1.2em
		max-height 500px
		overflow auto
</style>
