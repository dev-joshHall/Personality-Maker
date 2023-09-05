import { getPersonalies, getPersonality } from "./db-utils"

describe('getPersonalities() works', () => {
    it('gets all personalities', async() => {
        const personalities = await getPersonalies()
        console.log(personalities)

    })
})