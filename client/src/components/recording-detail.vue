<template>
	<article class="recording-detail">
		<h3 class="title">
			{{ recording.title }}
		</h3>
		<h4 class="description">
			{{ recording.artist }} 
			<span v-if="recording.isrc">
				({{ recording.isrc }})
			</span>
		</h4>
		<h5 class="duration" v-if="recording.duration">
			<i class="material-icons time">access_time</i>
			{{ recording.duration }}s
		</h5>
	</article>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator"

@Component
export default class RecordingDetail extends Vue {
	@Prop() recording: any
}
</script>

<style lang="stylus" scoped>
	.recording-detail
		padding .5em 0
		opacity 0.6
		transition opacity 0.3s
		&:hover
			opacity 0.9
	.title, .description
		text-transform uppercase
		font-size 15px
	.description
		font-size 85%
		opacity 0.8
		font-style italic
	.duration
		text-transform none
		font-size 75%
	.time
		font-size 14px
		position relative
		top 2.5px
</style>
