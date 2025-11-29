import 'package:flutter/material.dart';

class ChatListItem extends StatelessWidget {
  final String nome;
  final String ultimaMensagem;
  final String urlFoto;
  final String horario;

  const ChatListItem({
    super.key,
    required this.nome,
    required this.ultimaMensagem,
    required this.urlFoto,
    required this.horario,
  });

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: CircleAvatar(
        backgroundImage: NetworkImage(urlFoto),
        radius: 25,
      ),
      title: Text(
        nome,
        style: const TextStyle(fontWeight: FontWeight.bold),
      ),
      subtitle: Text(
        ultimaMensagem,
        style: const TextStyle(color: Colors.grey),
      ),
      trailing: Text(
        horario,
        style: const TextStyle(color: Colors.grey, fontSize: 12),
      ),
    );
  }
}
