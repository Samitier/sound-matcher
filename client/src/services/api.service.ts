import axios from "axios"

class ApiService {

	private readonly baseurl = "/api/"

	async getSearches() {
		return await this._get("searches")
	}

	async getSelectedMatches(searchId: string) {
		return await this._get("matches/" + searchId)
	}

	private async _get(url: string) {
		try {
			const { data } = await axios.get(this.baseurl + url)
			return data
		} catch (e) {
			// tslint:disable-next-line:no-console
			console.error(e)
		}
	}
}

export default new ApiService()

interface ModelData {
	fields: object
	model: string
	pk: number
}
