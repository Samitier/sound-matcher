<template>
	<section class="match-list" v-if="selectedMatches.length">
		<div 
			class="match"
			v-for="match in selectedMatches"
			:key="match.recording.id"
			:style="getStyle(match.score)"
		>
			<div class="score">
				{{ match.score }}%
			</div>
			<div>
				<RecordingDetail :recording="match.recording"/>
			</div>
		</div>
	</section>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import { State } from "vuex-class"
import Match from "@/models/match.model"
import RecordingDetail from "@/components/recording-detail.vue"

@Component({
	components: { RecordingDetail }
})
export default class MatchList extends Vue {
	@State selectedMatches: Match[]

	getStyle(score: number) {
		return {
			// Returns an opacity between .9 and .3 given the percentage of score
			opacity: Math.min(Math.max(score / 100, .3), .9)
		}
	}
}
</script>

<style lang="stylus" scoped>
	.match-list
		margin-top 2em
		background #f3f6e2
		border-radius 5px
		padding 1.2em
		text-align left
	.match
		display flex
		align-items center
	.score
		margin-right 1em
		padding-right 1em
		min-width 4em
		text-align right
		opacity 0.9
		font-weight bold
		font-size 100%
		border-right 1px solid #888	
</style>
