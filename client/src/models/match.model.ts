import Recording from "@/models/recording.model"

export default class Match {

	constructor(
		public id: string,
		public score: number,
		public recording: Recording
	) {}
}
