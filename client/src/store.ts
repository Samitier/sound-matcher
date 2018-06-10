import Vue from "vue"
import Vuex from "vuex"
import ApiService from "./services/api.service"
import Match from "@/models/match.model"
import Recording from "@/models/recording.model"

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		searches: [] as Recording[],
		selectedSearch: undefined as Recording,
		selectedMatches: [] as Match[]
	},
	mutations: {
		setSearches(state, searches: Recording[]) {
			state.searches.push(...searches)
		},
		setSelectedSearch(state, search: Recording) {
			state.selectedSearch = search
		},
		setSelectedMatches(state, matches: Match[]) {
			state.selectedMatches = matches
		},
	},
	actions: {
		async fetchSearches({ commit }) {
			const searches = await ApiService.getSearches()
			commit("setSearches", searches)
		},
		async selectSearch({ commit }, search) {
			commit("setSelectedSearch", search)
			const matches = await ApiService.getSelectedMatches(search.id)
			commit("setSelectedMatches", matches)
		}
	},
})
