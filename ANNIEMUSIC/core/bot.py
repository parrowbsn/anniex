from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
import config

from ..logging import LOGGER


class JARVIS(Client):
    def __init__(self):
        LOGGER(__name__).info("MUSICBROKN is initializing...")
        super().__init__(
            name="MUSICBROKN",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,  # Adjust as per your server capability
        )

    async def start(self):
        await super().start()

        # Fetch bot details
        self.id = self.me.id
        self.name = self.me.first_name + (f" {self.me.last_name}" if self.me.last_name else "")
        self.username = self.me.username
        self.mention = self.me.mention

        # Send startup message to the logger group/channel
        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} Bot Started:</b></u>\n\n"
                    f"🆔 ID: <code>{self.id}</code>\n"
                    f"📛 Name: {self.name}\n"
                    f"👤 Username: @{self.username}"
                ),
                parse_mode=ParseMode.HTML,
            )
        except errors.ChannelInvalid:
            LOGGER(__name__).error(
                "Invalid LOGGER_ID: Bot cannot access the log group/channel. Please check the LOGGER_ID."
            )
            exit(1)
        except errors.PeerIdInvalid:
            LOGGER(__name__).error(
                "Peer ID is invalid: Ensure LOGGER_ID is correctly set in the config file."
            )
            exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"Failed to send a message to the log group/channel. Reason: {type(ex).__name__}."
            )
            exit(1)

        # Check if the bot is an admin in the log group/channel
        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "Bot is not an admin in the log group/channel. Please promote the bot to admin."
                )
                exit(1)
        except errors.ChatAdminRequired:
            LOGGER(__name__).error(
                "ChatAdminRequired: The bot cannot verify admin status. Ensure the bot is added to the log group/channel."
            )
            exit(1)
        except errors.ChatWriteForbidden:
            LOGGER(__name__).error(
                "ChatWriteForbidden: Bot cannot write messages in the log group/channel. Check permissions."
            )
            exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"An error occurred while checking admin status in the log group/channel. Reason: {type(ex).__name__}."
            )
            exit(1)

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        # Log stop event
        LOGGER(__name__).info("Stopping MUSICBROKN bot...")
        try:
            await super().stop()
            LOGGER(__name__).info("MUSICBROKN bot has stopped successfully.")
        except Exception as ex:
            LOGGER(__name__).error(
                f"An error occurred while stopping the bot. Reason: {type(ex).__name__}."
            )
