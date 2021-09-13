import asyncio
import pytgcalls
import pyrogram
import streamlink
import sys


async def main(client):
    group_call = pytgcalls.GroupCallFactory(client).get_group_call()
    await group_call.join(sys.argv[3])
    stream = sys.argv[4]
    if not sys.argv[4].__contains__('m3u8'):
        stream = streamlink.streams(sys.argv[4])['720p'].url
    await group_call.start_video(stream)

    await pyrogram.idle()

if __name__ == '__main__':
    pyro_client = pyrogram.Client('user', sys.argv[1], sys.argv[2])
    pyro_client.start()
    pyro_client.get_dialogs()

    asyncio.get_event_loop().run_until_complete(main(pyro_client))
