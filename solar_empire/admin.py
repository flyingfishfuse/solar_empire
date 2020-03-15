import solar_empire

		out + "\t\t<tr>\n\t\t\t<td><label for=\"" + admin.username + "\">" +
		 admin.username + "</label>" + (in_array(admin.username, savedVars) ?
		 " <strong>Updated</strong>" : '') + "</td>\n\t\t\t<td>" +
		 adminVar['descript'] + "</td>\n\t\t\t<td>" + adminVar['min'] +
		 "</td>\n\t\t\t<td>" + adminVar['max'] +
		 "</td>\n\t\t\t<td><input type=\"text\" name=\"" +
		 admin.username + "\" id=\"" + admin.username + "\" value=\"" +
		 adminVar['value'] + "\" size=\"8\"></td>\n\t\t</tr>\n"

	</table>
</form>

