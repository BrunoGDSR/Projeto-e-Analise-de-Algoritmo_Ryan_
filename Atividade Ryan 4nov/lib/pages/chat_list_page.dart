import 'package:flutter/material.dart';
import '../widgets/chat_list_item.dart';

class ChatListPage extends StatelessWidget {
  const ChatListPage({super.key});

  @override
  Widget build(BuildContext context) {
    final List<Map<String, String>> chats = [
      {
        'nome': 'Jose Souza',
        'ultimaMensagem': 'Oi! Tudo bem?',
        'urlFoto': 'https://i.pravatar.cc/150?img=5',
        'horario': '14:32',
      },
      {
        'nome': 'Pedro Silva',
        'ultimaMensagem': 'Beleza, até amanhã!',
        'urlFoto': 'https://i.pravatar.cc/150?img=6',
        'horario': '13:15',
      }
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Lista de Chats'),
        
      ),
      body: ListView.builder(
        itemCount: chats.length,
        itemBuilder: (context, index) {
          final chat = chats[index];
         
          return ChatListItem(
            nome: chat['nome']!,
            ultimaMensagem: chat['ultimaMensagem']!,
            urlFoto: chat['urlFoto']!,
            horario: chat['horario']!,
          );
        },
      ),
    );
  }
}