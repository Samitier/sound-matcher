<template>
	<section>
		<div 
			v-for="match in selectedMatches"
			:key="match.recording.id"
		>
			{{ match.score }}
			<RecordingDetail :recording="match.recording"/>
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

}
</script>

<style lang="stylus" scoped>
	
</style>
